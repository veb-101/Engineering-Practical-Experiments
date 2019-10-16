create table employee(id int primary key, name varchar(30), salary int, gender varchar(10), departmentid int);

insert into employee values (1, 'X', 5000, 'M', 3);
insert into employee values (2, 'y', 5400, 'F', 2);
insert into employee values (3, 'z', 2000, 'M', 1);
insert into employee values (4, 'a', 6000, 'F', 2);

create table employeeAudit(id int IDENTITY(1, 1) primary key, auditData varchar(1000), auditDate DATETIME);

create trigger tr_emp_for_insert BEFORE INSERT ON  employee
begin 
	declare @id int
	declare @name varchar(100)
	declare @auditData varchar(100)
	select @id =id, @name=name from inserted
	set @auditData = 'New Employee added with ID: ' + cast(@id as varchar(10)) + ' and Name: ' + @name
	insert into employeeAudit(auditData, auditDate) values(@auditData, GETDATE())
end

insert into employee values(6, 'B', 3300, 'M', 2);
select * from employeeAudit;

create table stud67(tid int, name varchar(20), subj1 int, subj2 int, total int, per int);

create trigger studmarks67 on stud67 after insert, update as RAISERROR('Enter correct marks', 8, 8);

insert into stud67 values(1, 'abcde', 5, 6, 40, 100);
