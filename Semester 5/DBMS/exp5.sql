---- Primary key constraint
select ' --------------------------------------';
create table samsung(ID int not null, model varchar(255), price int, primary key (ID));
insert into samsung values (1, 'galaxy', 4000);
select * from samsung;
-- insert into samsung values (1, 'test', 43000);
----gives  error 'Violation of PRIMARY KEY constraint'


--- ignore the following line
PRAGMA foreign_keys = ON;
---- Foreign key constraint
select ' --------------------------------------';
create table samsung2(model_id int, model varchar(255), price int, primary key(model_id));

create table orders1(order_id int, order_no int, model_id int, primary key(order_id), 
                        foreign key (model_id) references samsung2(model_id));

insert into samsung2 values(1, 'galaxy', 23123);
insert into samsung2 values(2,'note', 2322);

insert into orders1 values (50, 400 ,1);
select * from orders1;
-- insert into orders1 values (45, 450 ,3);
----gives error "The INSERT statement conflicted with the FOREIGN KEY constraint"

---- Default key constraint
select ' --------------------------------------';
create table Ig2(model_id int not null, model varchar(255), price int default(70000));
insert into Ig2 values(1, 'galaxy', 40000);
insert into Ig2 (model_id, model) values (2, 'galaxy');
select * from Ig2;

---- Check constraint
select ' --------------------------------------';
create table Ig4(model_id int not null, model varchar(255), price int, Check(price>=50000));
insert into Ig4 values(1, 'galaxy', 80000);
select * from Ig4
-- insert into Ig4 values(2, 'test', 40000);
----gives error 'insert into Ig4 values(1, 'galaxy', 80000);'