CREATE TABLE users(
  userID int not null auto_increment,
  username varchar(50),
  userPin varchar(100),
  supervisor varchar(50),
  department varchar(50),
  faculty varchar(50),
  institution varchar(50),
  rateType varchar(50),
  Permissions varchar(7),
  PRIMARY KEY (userID)
);

CREATE TABLE alerted(
  alertID int not null auto_increment PRIMARY KEY,
  machine varchar(50),
  machineName varchar(50),
  timeUsed datetime,
  userID varchar(50),
  userName varchar(100)
);



CREATE TABLE entries(
  entrieID int not null auto_increment PRIMARY KEY,
  machine varchar(50),
  timeUsed datetime,
  userID varchar(50),
  inUse boolean,
  enteredSession boolean
);

CREATE TABLE openCardNumber(
  cardID int not null auto_increment PRIMARY KEY,
  cardNumber varchar(50),
  timeUsed datetime
);


CREATE TABLE machines(
  machine varchar(50),
  name varchar(100),
  inUse boolean,
  academicRate decimal(8,2),
  institutionalRate decimal(8,2),
  machineID int not null auto_increment PRIMARY KEY
);

CREATE TABLE machine1 (
  userID varchar(50));

CREATE TABLE machine2 (
  userID varchar(50));

CREATE TABLE machine3 (
  userID varchar(50));

CREATE TABLE machine4 (
  userID varchar(50));

CREATE TABLE machine5 (
  userID varchar(50));

CREATE TABLE machine6 (
  userID varchar(50));

CREATE TABLE machine7 (
  userID varchar(50));

CREATE TABLE supervisors (
  superID int not null auto_increment,
  superName varchar(50),
  PRIMARY KEY (superID)
);


CREATE TABLE departments (
  deptID int not null auto_increment,
  deptName varchar(50),
  PRIMARY KEY (deptID)
);

CREATE TABLE faculty (
  facultyID int not null auto_increment,
  facultyName varchar(50),
  PRIMARY KEY (facultyID)
);

CREATE TABLE institution (
  institutionID int not null auto_increment,
  institutionName varchar(50),
  PRIMARY KEY (institutionID)
);


CREATE TABLE rateType (
  rateID int not null auto_increment,
  rateName varchar(50),
  rateAmount varchar(50),
  PRIMARY KEY (rateID)
);


CREATE TABLE sessions (
  sessionID int not null auto_increment PRIMARY KEY,
  machineID varchar(50),
  machineName varchar(100),
  sessionStart datetime,
  sessionEnd datetime,
  timeUsed varchar(20),
  rateUsed varchar(50),
  rateTypeUsed varchar(50),
  billAmount varchar(20),
  userID varchar(100),
  userName varchar(50)
);


INSERT INTO rateType (rateName, rateAmount) values ("Academic", "Academic Machine Dependant");
INSERT INTO rateType (rateName, rateAmount) values ("Institutional", "Institutional Machine Dependant");  

INSERT INTO machines(machine, name, inUse, academicRate, institutionalRate) VALUES('98:01:a7:8f:00:99', 'Oxford Lasers Micromachining Laser', '0',66.99, 99.25);
INSERT INTO machines(machine, name, inUse, academicRate, institutionalRate) VALUES('b8:27:eb:61:98:05', 'Raith Pioneer Electron-beam', '0', 6, 99);
INSERT INTO machines(machine, name, inUse, academicRate, institutionalRate) VALUES('00:00:00:00:00:03', 'NxQ 4006 Mask Aligner', '0',6, 99);
INSERT INTO machines(machine, name, inUse, academicRate, institutionalRate) VALUES('00:00:00:00:00:04', 'IMP SF-100 Xpress Maskless Photolithography System','0', 6, 99);
INSERT INTO machines(machine, name, inUse, academicRate, institutionalRate) VALUES('00:00:00:00:00:05', 'Trion MiniLock III Reactive Ion Etcher', '0', 6, 99);
INSERT INTO machines(machine, name, inUse, academicRate, institutionalRate) VALUES('00:00:00:00:00:06', 'PVD 75 Sputtering System','0',66, 99);
INSERT INTO machines(machine, name, inUse, academicRate, institutionalRate) VALUES('00:00:00:00:00:07', 'Thermionics electron-beam Evaporator', '0', 66, 99);
