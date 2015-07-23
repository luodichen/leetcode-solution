# https://leetcode.com/problems/employees-earning-more-than-their-managers/
# Write your MySQL query statement below
SELECT a.Name FROM Employee AS `a`
INNER JOIN Employee AS `b` ON a.ManagerId = b.Id
WHERE a.Salary > b.Salary;
