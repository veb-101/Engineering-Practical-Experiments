create table employee98(id int primary key, name varchar(10), age int, address varchar(10), salary int);

insert into employee98 values (1, 'p', 30, 'a', 20);
insert into employee98 values (2, 'q', 40, 'b', 70);
insert into employee98 values (3, 'r', 20, 'c', 10);
insert into employee98 values (4, 's', 10, 'd', 30);
insert into employee98 values (5, 't', 50, 'e', 40);

-- select * from employee98;


select "EXAMPLE RUN";

SELECT * FROM employee98 WHERE ID IN (SELECT ID FROM employee98 WHERE SALARY > 10);


select "________________________________________";

create table project(Proj_id int,Proj_name varchar(50));
create table employee(Emp_id int,Emp_name varchar(30));
create table alloc_to(Proj_id int,Emp_id int);

insert into project values(100,'TCS');
insert into project values(200,'Infosys');
insert into project values(300,'Capgemini');

insert into employee values(1,'Virag');
insert into employee values(2,'Raj');
insert into employee values(3,'Ravi');
insert into employee values(4,'Aman');
insert into employee values(5,'Dev');

insert into alloc_to values(100,1);
insert into alloc_to values(200,1);
insert into alloc_to values(300,1);
insert into alloc_to values(100,2);
insert into alloc_to values(200,2);
insert into alloc_to values(100,3);
insert into alloc_to values(200,3);
insert into alloc_to values(300,3);
insert into alloc_to values(100,4);
insert into alloc_to values(200,4);
insert into alloc_to values(100,5);
insert into alloc_to values(300,5);


select "----QUERY 1----";
select e.Emp_id,e.Emp_name,p.Proj_id,p.Proj_name from employee as e,project as p,alloc_to as a where a.Proj_id = p.Proj_id and a.Emp_id = e.Emp_id;

select "----QUERY 2----";
select * from employee where Emp_id in (select Emp_id from alloc_to where Proj_id = 100);

select "----QUERY 3----";
select * from employee where Emp_id in (select Emp_id from alloc_to as a,project as p where a.Proj_id = p.Proj_id and Proj_name = 'Capgemini');

select "----QUERY 4----";
select * from employee where Emp_id in (select Emp_id from alloc_to where Proj_id = 100) and Emp_id in (select Emp_id from alloc_to where Proj_id = 200);

select "----QUERY 5----";
select * from employee where Emp_id not in (select Emp_id from alloc_to where Proj_id = 200);

select "----QUERY 6----";
select distinct Emp_id from alloc_to where Proj_id in(select Proj_id from alloc_to where Emp_id = 5);