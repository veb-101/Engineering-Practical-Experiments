---------DDL Commands----------
-- drop table Person;
create table Person(name varchar(20), address varchar(20));
alter table Person add age varchar(2);
--truncate table Person;
--drop table Person
-- EXEC sp_help 'Person'

----------DML Commands---------
insert into Person values('Vaibhav', 'Goregaon', 10);
insert into Person values('Lokesh', 'Kandivali', 10);
insert into Person values('Hades', 'HELL', 10);
insert into Person values('Zeus', 'Olympus', 10);
select * from Person;
select ' -----------------------------';
update Person set address='NAGALAND' where address='Kandivali';
select * from Person;
select ' -----------------------------';
insert into Person(name, address) values ('Test', 'T20');
update Person set age=10 where name='Test';
select * from Person;
select ' -----------------------------';
delete from Person where name='Vaibhav';
select * from Person; 