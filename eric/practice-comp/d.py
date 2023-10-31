CREATE DATABASE Royals2;
use royals2;
CREATE table royalFamily (
name varchar(20),
active_indicator bit not null,
salary decimal(8,2) null,
PRIMARY KEY (name)
);
INSERT INTO royalFamily values ('william',1,100000);
INSERT INTO royalFamily values ('kate',1,200000);
INSERT INTO royalFamily values ('harry',1,300000);



CREATE TABLE engagements (
 EngagementName varchar(40),
 StartDate datetime,
 royalFamilyName varchar(20)
);

insert into engagements values ('Save the Penguins','2022-10-01 11:00:00','william');
insert into engagements values ('Constituent Complaints','2020-10-19 11:00:00','kate');
insert into engagements values ('Lunch With Presidents','2022-09-01 14:00:00','kate');
insert into engagements values ('Kissing Babies','2022-04-01 12:00:00','harry');
insert into engagements values ('Kissin