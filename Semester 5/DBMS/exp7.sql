create table emp15(id int, name varchar(50), salary int);

insert into emp15 values (1, 'a', 10000);
insert into emp15 values (2, 'b', 20000);
insert into emp15 values (3, 'c', 30000);
insert into emp15 values (4, 'd', 15000);
insert into emp15 values (5, 'e', 18000);


create table emp10(id int, name varchar(50), age int);

insert into emp10 values (4, 'a', 10);
insert into emp10 values (5, 'b', 20);
insert into emp10 values (32, 'c', 30);
insert into emp10 values (43, 'd', 15);
insert into emp10 values (56, 'e', 20);


-- Aggregate function
select count(salary) from emp15;
select avg(salary)  from emp15;
select sum(salary) from emp15;
select min(salary) from emp15;
select max(salary) from emp15;

-- Single View 
select '----------------------------------'; 
select '--------- Single View ------------'; 
create view data as select id, name from emp15 where id < 3;

select * from data;


-- Multiple view
select '----------------------------------'; 
select '--------- Multiple View -----------';

create view test as select emp15.Name, emp15.salary, emp10.age from emp10, emp15 where emp10.name == emp15.name;

select * from test;

