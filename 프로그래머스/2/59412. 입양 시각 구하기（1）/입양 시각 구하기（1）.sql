-- 코드를 입력하세요
SELECT HOUR(DATETIME) as HOUR, COUNT(*) as COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR
HAVING HOUR BETWEEN 9 AND 19
ORDER BY HOUR ASC
