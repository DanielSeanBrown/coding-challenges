SELECT DISTINCT CITY
FROM STATION
WHERE NOT RIGHT(CITY, 1) IN ('a', 'e', 'i', 'o', 'u')
    OR NOT LEFT(CITY, 1) IN ('a', 'e', 'i', 'o', 'u');
