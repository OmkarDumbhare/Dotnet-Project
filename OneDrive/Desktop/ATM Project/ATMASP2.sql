create database ATMASPX
Go
use ATMASPX
Go
create table LoginTab1
(
   LoginId int identity primary key,
   Actno int not null,
   Pinno int not null,
   AccountHolder varchar(40) not null
)
Go
insert into LoginTab1 values(101,101,'Prince')
insert into LoginTab1 values(102,102,'Jasraj')
insert into LoginTab1 values(501,501,'MSEB')
insert into LoginTab1 values(502,502,'BSNL')
insert into LoginTab1 values(503,503,'LIC')
Go
create table Trasac1
(
   TransId int identity primary key,
   Actno int not null,
   DOT varchar(40) not null,
   Deposit int not null,
   Withdraw int not null,
   Trans int not null
)
Go
--Deposit
insert into Trasac1 values(101,'30-10-2021',10000,0,0)
--Withdrawl
insert into Trasac1 values(101,'31-10-2021',0,1000,0)
--Transfer
insert into Trasac1 values(101,'01-11-2021',0,0,5000)
insert into Trasac1 values(102,'01-11-2021',5000,0,0)
Go
select * from LoginTab1
select * from Trasac1
Go
--Balance
Select sum(Deposit) - sum(Withdraw) -sum(Trans) From Trasac1 where Actno=101

---
use ATMASPX
GO
create table MSE
(
   Id int identity primary key,
   Billno int not null,
   Billamt int not null,
   Custname varchar(30) not null
)
GO
insert into MSE values(101,1500,'prince')
insert into MSE values(102,500,'naman')
insert into MSE values(103,1000,'parv')
insert into MSE values(104,800,'yash')
GO
create  table Billback
(
   Id int identity primary key,
   Billno int not null,
   Billamt int not null,
   Billtype varchar(40) not null,
   Actno int not null,
   DOT varchar(30) not null
)
GO
