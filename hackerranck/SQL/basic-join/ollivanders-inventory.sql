SELECT W.id, WP.age, W.coins_needed, W.power
FROM Wands W
INNER JOIN Wands_Property WP
ON W.code = WP.code
WHERE WP.is_evil = 0 
    AND W.coins_needed = (SELECT MIN(V.coins_needed)
                              FROM Wands V
                              INNER JOIN Wands_Property VP
                              ON V.code = VP.code
                              WHERE V.power = W.power AND VP.age = WP.age) 
ORDER BY W.power DESC, WP.age DESC;
