# %%
import pandas as pd

# %%
df = pd.read_csv("../data/raw/raw_data.csv")
df

# %%
df['count_of_facility_pt_exp_measures'].unique()

# %%
df = pd.read_csv("../data/raw/raw_data.csv", na_values=['Not Available'])
df['count_of_facility_pt_exp_measures'].unique()

# %%
df.info()

# %%
df['state']

# %%
ga_hospitals_df = df.loc[df['state'].str.contains('GA')].sort_values("facility_name").reset_index(drop=True)
ga_hospitals_df

# %%
ga_hospitals_df.columns

# %%
ga_hospitals_df.drop(columns=['hospital_overall_rating_footnote', 'mort_group_measure_count','mort_group_footnote', 'safety_group_measure_count', 'safety_group_footnote', 'readm_group_measure_count', 'readm_group_footnote', 'pt_exp_group_measure_count', 'pt_exp_group_footnote', 'te_group_measure_count', 'te_group_footnote' , 'telephone_number' ], inplace=True)

# %%
ga_hospitals_df

# %%
missing_values=ga_hospitals_df.isnull().sum()
missing_values


# %%
ga_hospitals_df.info()

# %%
ga_hospitals_df.describe()

# %%
ga_county_hosp_df = ga_hospitals_df.groupby('countyparish')
ga_county_hosp_df.count()

# %%
ga_hospitals_df.rename(columns={'countyparish': 'county'}, inplace=True)

# %%
ga_hospitals_df

# %%
ga_hospitals_df['hospital_overall_rating'] = pd.to_numeric(ga_hospitals_df['hospital_overall_rating'], errors="coerce")
ga_hospitals_df['hospital_overall_rating']

# %%
ga_hospitals_df['emergency_services'] = ga_hospitals_df['emergency_services'].replace({'Yes': True, 'No':False}).astype(bool)


# %%
ga_hospitals_df['zip_code'] = ga_hospitals_df['zip_code'].astype(str).str.zfill(5)

# %%
ga_hospitals_df.groupby('hospital_ownership').count()

# %%
ga_hospitals_df.columns

# %%
ga_hospitals_df

# %%
ga_hospital_perfomance = ga_hospitals_df[['facility_id','count_of_facility_mort_measures','count_of_mort_measures_better', 'count_of_mort_measures_no_different','count_of_mort_measures_worse', 'count_of_facility_safety_measures','count_of_safety_measures_better','count_of_safety_measures_no_different','count_of_safety_measures_worse', 'count_of_facility_readm_measures','count_of_readm_measures_better','count_of_readm_measures_no_different', 'count_of_readm_measures_worse','count_of_facility_pt_exp_measures', 'count_of_facility_te_measures']]

# %%
ga_hospital_perfomance

# %%
ga_hospitals_df.drop(columns=['count_of_facility_mort_measures','count_of_mort_measures_better', 'count_of_mort_measures_no_different','count_of_mort_measures_worse', 'count_of_facility_safety_measures','count_of_safety_measures_better','count_of_safety_measures_no_different','count_of_safety_measures_worse', 'count_of_facility_readm_measures','count_of_readm_measures_better','count_of_readm_measures_no_different', 'count_of_readm_measures_worse','count_of_facility_pt_exp_measures', 'count_of_facility_te_measures'], inplace=True)

# %%
ga_hospitals_df

# %%
ga_hospitals_df['meets_criteria_for_birthing_friendly_designation'].unique()

# %%
ga_hospitals_df.to_csv("../data/clean/ga_hospitals.csv", index=False, encoding='utf-8')

# %%
ga_hospital_perfomance.to_csv("../data/clean/ga_hospitals_performance.csv", index=False, encoding='utf-8')


