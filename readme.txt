 STUDENTS ACADEMIC PROFILE MANAGEMENT SYSTEM
 -devloped by AnkitAmbasta
 -ankitambasta862004@gmail.com

Instructions-
(i)under the  #Connection statement ,do following changes
import mysql.connector  
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="your_username",
  passwd ="your_passwd",
  database="database_name")
(ii)create a table in mysql in mysql as described at your working database
+------------+---------------+------+-----+---------+-------+
| Field      | Type          | Null | Key | Default | Extra |
+------------+---------------+------+-----+---------+-------+
| RollNo     | int           | NO   | PRI | NULL    |       |
| Name       | char(30)      | YES  |     | NULL    |       |
| Physics    | decimal(10,0) | NO   |     | NULL    |       |
| Chemistry  | decimal(10,0) | NO   |     | NULL    |       |
| Maths      | decimal(10,0) | NO   |     | NULL    |       |
| English    | decimal(10,0) | NO   |     | NULL    |       |
| CS         | decimal(10,0) | NO   |     | NULL    |       |
| Total      | decimal(10,0) | YES  |     | NULL    |       |
| Percentage | decimal(10,0) | YES  |     | NULL    |       |
+------------+---------------+------+-----+---------+-------+
(iii)it is recommended to create table by name ("report")
OR
under #sql change report to (your_tablename)

my sql table......
 create table report
(RollNo int not null primary key,
Name varchar(30) not null,
Physics decimal not null,
Chemistry decimal not null,
Maths decimal not null,
English decimal not null,
CS decimal not null,
Total decimal,
Percentage decimal);


Limitations
(i)Programme will throw an error when wrong datatype is entered
for eg. a string in place of an integer
(ii)

apology for poor english
