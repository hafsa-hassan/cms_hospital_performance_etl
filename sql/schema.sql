IF NOT EXISTS
    (
        SELECT name FROM sys.databases WHERE name = 'cms_hospital_db'
    )
BEGIN
    CREATE DATABASE cms_hospital_db
END;

CREATE SCHEMA hospital;

CREATE TABLE hospital.information(
    facility_id VARCHAR(20) PRIMARY KEY,
    facility_name VARCHAR(255),
    address VARCHAR(255),
    citytown VARCHAR(255),
    state CHAR(2),
    zip_code CHAR(5),
    county VARCHAR(255),
    hospital_type VARCHAR(255),
    hospital_ownership VARCHAR(255),
    emergency_services BIT,
    meets_criteria_for_birthing_friendly_designation VARCHAR(50),
    hospital_overall_rating FLOAT
)

CREATE TABLE hospital.performance(
    facility_id VARCHAR(20) NOT NULL,
    count_of_facility_mort_measures FLOAT,
    count_of_mort_measures_better FLOAT,
    count_of_mort_measures_no_different FLOAT,
    count_of_mort_measures_worse FLOAT,
    count_of_facility_safety_measures FLOAT,
    count_of_safety_measures_better FLOAT,
    count_of_safety_measures_no_different FLOAT,
    count_of_safety_measures_worse FLOAT,
    count_of_facility_readm_measures FLOAT,
    count_of_readm_measures_better FLOAT,
    count_of_readm_measures_no_different FLOAT,
    count_of_readm_measures_worse FLOAT,
    count_of_facility_pt_exp_measures FLOAT,
    count_of_facility_te_measures FLOAT,
    FOREIGN KEY(facility_id) REFERENCES hospital.information(facility_id)

)

CREATE TABLE hospital.mspb(
    facility_id VARCHAR(20) NOT NULL,
    measure_id VARCHAR(20),
    score FLOAT,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY(facility_id) REFERENCES hospital.information(facility_id)
)