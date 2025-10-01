SELECT 
    CAST(SUM(CASE WHEN emergency_services = 1 THEN 1 ELSE 0 END) *100 / COUNT (*) AS DECIMAL(5,2)) 
    AS perc_with_emergency,
    CAST(SUM(CASE WHEN emergency_services = 0 THEN 1 ELSE 0 END) *100 / COUNT (*) AS DECIMAL(5,2))
    AS perc_without_emergency
FROM hospital.information

-- percent of hospitals better than national mortality
SELECT
    ROUND((COUNT(CASE WHEN count_of_mort_measures_better > 0 THEN 1 END) *1.0 / COUNT( DISTINCT facility_id) * 100),2) AS pct_hospitals_better_mort
FROM hospital.performance
WHERE count_of_facility_mort_measures > 0