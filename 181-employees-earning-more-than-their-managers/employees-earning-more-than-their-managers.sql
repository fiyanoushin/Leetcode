-- Write your PostgreSQL query statement below
select e.name as Employee
from Employee e
inner join Employee m
on e.managerId=m.Id
where e.salary>m.salary;