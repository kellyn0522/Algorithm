-- 코드를 작성해주세요
SELECT count(*) as COUNT
FROM ECOLI_DATA
WHERE GENOTYPE & 2 = 0  and (GENOTYPE & 1 != 0 or GENOTYPE & 4 != 0)