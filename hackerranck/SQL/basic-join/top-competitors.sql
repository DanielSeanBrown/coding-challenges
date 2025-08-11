SELECT H.hacker_id, H.name
FROM Hackers H

INNER JOIN Submissions S
ON H.hacker_id = S.hacker_id
INNER JOIN Challenges C
ON S.challenge_id = C.challenge_id
LEFT JOIN Difficulty D
ON C.difficulty_level = D.difficulty_level

WHERE S.score = D.score AND C.difficulty_level = D.difficulty_level

GROUP BY H.hacker_id, H.name
HAVING COUNT(S.hacker_id) > 1

ORDER BY COUNT(S.hacker_id) DESC, S.hacker_id ASC;
