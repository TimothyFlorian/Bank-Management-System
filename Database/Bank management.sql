USE bank_management;
--------------------------------------------------------

	-- TABLE CREATION :

CREATE TABLE Customer(
custid VARCHAR(100),
pass VARCHAR(100),
CONSTRAINT custid_pk PRIMARY KEY(custid));

DESC Customer;

CREATE TABLE Staff(
staffid VARCHAR(100),
passwd VARCHAR(100),
CONSTRAINT staffid_pk PRIMARY KEY(staffid));

DESC Staff;

CREATE TABLE Acc(
acc_no VARCHAR(20),
fname VARCHAR(100),
lname VARCHAR(100),
dob VARCHAR(10),
acc_type VARCHAR(10),
amount INT,
address VARCHAR(100),
phone_no NUMERIC(10),
sex VARCHAR(20),
CONSTRAINT acc_no_pk PRIMARY KEY(acc_no));

DESC Acc;

-------------------------------------------------------------------

		-- INSERTING RECORDS :

INSERT INTO Staff VALUES('Timothy Florian','tim#12');
INSERT INTO Staff VALUES('Jospar Millian','jos#13');
INSERT INTO Staff VALUES('Rohit','roh#14');

INSERT INTO Customer VALUES('Liam','lia#l');
INSERT INTO Customer VALUES('Alison','ali#a');
INSERT INTO Customer VALUES('Scott','sco#s');


-------------------------------------------------------------------


















-------------------------------------------------------------------
SELECT * FROM Staff;
SELECT * FROM Customer;
SELECT * FROM Acc;
DROP TABLE Customer;
DROP TABLE Staff;
DROP TABLE Acc;
TRUNCATE TABLE Customer;
TRUNCATE TABLE Staff;
TRUNCATE TABLE Acc;