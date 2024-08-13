create database registeration;
use registeration;
create table sigin(
id int not null auto_increment,
name varchar(50) not null,
email varchar(50) not null,
age int not null,
contact_number int not null,
password varchar(50) not null,
primary key(id)
);
alter table sigin modify contact_number varchar(25) not null;
describe sigin;
insert into sigin(id,name,email,age,contact_number,password) values(1,"venkat","venkat@123",24,9626453525,"venkat@123");
select * from sigin;
