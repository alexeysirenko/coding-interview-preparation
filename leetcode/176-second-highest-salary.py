# Write your MySQL query statement below
SELECT IFNULL(

(SELECT DISTINCT
Salary
FROM Employee
ORDER BY Salary DESC
LIMIT 1, 1),

NULL)  AS SecondHighestSalary

#select max(salary) as SecondHighestSalary
#from Employee
#where salary < (select max(salary) from Employee)