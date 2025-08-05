SELECT DISTINCT CITY
FROM STATION
WHERE NOT LEFT(CITY, 1) IN ('A', 'E', 'I', 'O', 'U')
    AND NOT RIGHT(CITY, 1) IN ('a', 'e', 'i', 'o', 'u');
