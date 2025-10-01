
---Better performance in hospitals

SELECT
    i.facility_name,
    ROUND(((P.count_of_mort_measures_better *1.0/P.count_of_facility_mort_measures) * 100),2) AS score,
     'Mortality' AS measure_type, 'Better' AS performance_type
FROM hospital.performance AS p
JOIN hospital.information AS i
ON p.facility_id = i.facility_id
WHERE P.count_of_mort_measures_better IS NOT NULL

UNION ALL

SELECT
    i.facility_name,
    ROUND(((P.count_of_readm_measures_better * 1.0/P.count_of_facility_readm_measures) * 100),2),
     'Readmission', 'Worse'
FROM hospital.performance AS p
JOIN hospital.information AS i
ON p.facility_id = i.facility_id
WHERE P.count_of_readm_measures_better IS NOT NULL

UNION ALL

SELECT
    i.facility_name,
    ROUND(((P.count_of_safety_measures_better * 1.0/P.count_of_facility_safety_measures) * 100),2),
     'Safety', 'No different'
FROM hospital.performance AS p
JOIN hospital.information AS i
ON p.facility_id = i.facility_id
WHERE P.count_of_safety_measures_better IS NOT NULL
ORDER BY score DESC



-- Top 5 cost efficient hospitals


SELECT TOP 5 WITH TIES
    i.facility_name,score
FROM hospital.mspb AS m
JOIN hospital.information AS i
ON m.facility_id = i.facility_id
WHERE score IS NOT NULL
ORDER BY score ASC

