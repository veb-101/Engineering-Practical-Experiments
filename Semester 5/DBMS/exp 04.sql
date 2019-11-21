---------DDL Commands----------
-- drop table Person;
create table Person(name varchar(20), address varchar(20));
alter table Person add age varchar(2);
--truncate table Person;
--drop table Person
-- EXEC sp_help 'Person'
alter table Person rename to Per;
-- alter table Per rename column age to AGE;
-- alter table Per drop column AGE;
-- alter table Per modify age varchar(3);

----------DML Commands---------
insert into Per values('Vaibhav', 'Goregaon', 10);
insert into Per values('Lokesh', 'Kandivali', 10);
insert into Per values('Hades', 'HELL', 10);
insert into Per values('Zeus', 'Olympus', 10);
select * from Per;
select ' -----------------------------';
update Per set address='NAGALAND' where address='Kandivali';
select * from Per;
select ' -----------------------------';
insert into Per(name, address) values ('Test', 'T20');
update Per set age=10 where name='Test';
select * from Per;
select ' -----------------------------';
delete from Per where name='Vaibhav';
select * from Per; 