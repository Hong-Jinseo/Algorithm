-- SQL 고득점 Kit : IS NULL

-- 01 경기도에 위치한 식품창고 목록 출력하기
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, IFNULL(FREEZER_YN, 'N')  AS FREEZER_YN
FROM FOOD_WAREHOUSE
WHERE LEFT(ADDRESS, 3) = '경기도'
ORDER BY WAREHOUSE_ID;


-- 02 이름이 없는 동물의 아이디
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL
ORDER BY ANIMAL_ID;


-- 03 이름이 있는 동물의 아이디
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
ORDER BY ANIMAL_ID;


-- 04 NULL 처리하기
SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name') AS NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS;


-- 05 나이 정보가 없는 회원 수 구하기
SELECT COUNT(*) AS USERS
FROM USER_INFO
WHERE AGE IS NULL;