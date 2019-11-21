-- STRING OPERATIONS
create table emp(id int, name varchar(20), city varchar(20));
alter table emp add salary int;
insert into emp values(1, 'sam', 'mumbai', 40000);
insert into emp values(2, 'smith', 'jaipur', 50000);
insert into emp values(3, 'sean', 'mumbai', 45000);

SELECT ' --------------------------------------';
select * from emp;
SELECT ' --------------------------------------';
select * from emp where name like 's%';
SELECT ' --------------------------------------';
select * from emp where name like 'sm%';
SELECT ' --------------------------------------';
select * from emp where name like '%n';
SELECT ' --------------------------------------';
select * from emp where name like '%a%';
SELECT ' --------------------------------------';
select * from emp where name like '_a%';
SELECT ' --------------------------------------';
select * from emp where name like '%t_';
SELECT ' --------------------------------------';
select * from emp where name not like '%a%';

-- SET OPERATIONS
create table Stud2(name varchar(15),totalMark int);
create table Stud5(name varchar(15),totalMark int);

insert into Stud2 values('Robert',1063);
insert into Stud2 values('John',1070);
insert into Stud2 values('Rose',1032);
insert into Stud2 values('Abel',1002);

insert into Stud5 values('Robert',1063);
insert into Stud5 values('Rose',1032);
insert into Stud5 values('Boss',1086);
insert into Stud5 values('Marry',1034);

select * from Stud2 UNION select * from Stud5; -- doesn't allow duplicates

-- select * from Stud2 UNIONALL select * from Stud5; -- allows duplicates

select * from Stud2 INTERSECT select * from Stud5;

-- select * from Stud2 minus select * from Stud5; -- sql server
select * from Stud2 except select * from Stud5;