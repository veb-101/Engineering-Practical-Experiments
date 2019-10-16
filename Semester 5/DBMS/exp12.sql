create table Employee20(id int, name varchar(20), salary int);

create table Project20(pid int, name varchar(20));

insert into Employee20 values (1, 'a', 50000);
insert into Employee20 values (2, 'b', 70000);
insert into Employee20 values (3, 'c', 30000);

insert into Project20 values (4, 'd');
insert into Project20 values (2, 'b');
insert into Project20 values (3, 'c');


select * from Employee20;

select '-----------------';

select * from Project20;


select '------------LEFT OUTER JOIN--------------';
select Employee20.name, Project20.pid from Employee20 left outer join Project20 on Employee20.id = Project20.pid order by Employee20.name;

select '-----------RIGHT OUTER JOIN--------------';
select Employee20.name, Project20.pid from Employee20 right outer join Project20 on Employee20.id = Project20.pid order by Employee20.name;

select '-----------FULL OUTER JOIN--------------';
select Employee20.name, Project20.pid from Employee20 full outer join Project20 on Employee20.id = Project20.pid order by Employee20.name;
