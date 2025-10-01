from sqlalchemy import create_engine, text
import pandas as pd
from dotenv import load_dotenv
import os
import urllib

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_SERVER = os.getenv("DB_SERVER")
DB_NAME = os.getenv("DB_NAME")

#connecting to SQL server

params = urllib.parse.quote_plus(
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={DB_SERVER};'
    f'DATABASE={DB_NAME};'
    f'UID={DB_USER};'
    f'PWD={DB_PASSWORD}'
)
engine = create_engine(f'mssql+pyodbc:///?odbc_connect={params}')


# CSV file paths to load

df_info = pd.read_csv("data/clean/ga_hospitals_info.csv")
df_perf = pd.read_csv("data/clean/ga_hospitals_performance.csv")
df_mspb = pd.read_csv("data/clean/ga_hospitals_mspb.csv")

with engine.connect() as conn:

    conn.execute(text("DELETE FROM hospital.mspb;"))
    conn.execute(text("DELETE FROM hospital.performance;"))
    conn.execute(text("DELETE FROM hospital.information"))

    print("All rows deleted safely")


# loading from panda dataframe to sql

df_info.to_sql('information', engine, schema='hospital', if_exists='append', index=False)
df_perf.to_sql('performance', engine, schema='hospital', if_exists='append', index=False)
df_mspb.to_sql('mspb', engine, schema='hospital', if_exists='append', index=False)
