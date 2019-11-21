--- ignore the following line
PRAGMA foreign_keys = ON;
---- Foreign key constraint

create table dept67(did int, dnmae varchar(20), primary key(did));
create table Emp67(empid int, ename varchar(20), did int, primary key(empid), foreign key(did) references dept67 on delete cascade on update cascade);

insert into dept67 values(1, 'a');
insert into dept67 values(2, 'b');
insert into dept67 values(3, 'bz');

insert into Emp67 values(1, 'ab', 1);
insert into Emp67 values(2, 'abc', 2);
insert into Emp67 values(3, 'abfc', 3);

insert into Emp67 values(4, 'abfc', 4);
