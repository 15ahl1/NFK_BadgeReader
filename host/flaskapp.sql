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
  industrialRate decimal(8,2),
  machineID int not null auto_increment PRIMARY KEY
);

CREATE TABLE OxfordLaserPer (
  userID varchar(50));

CREATE TABLE RaithBeamPer (
  userID varchar(50));

CREATE TABLE NxQAlignerPer (
  userID varchar(50));

CREATE TABLE IMPSystemPer (
  userID varchar(50));

CREATE TABLE TrionEtcherPer (
  userID varchar(50));

CREATE TABLE PVDSystemPer (
  userID varchar(50));

CREATE TABLE ThermionicsPer (
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


INSERT INTO supervisors (superName) values ("Graham Gibson");
INSERT INTO departments (DeptName) values ("Computer Science");
INSERT INTO faculty (facultyName) values ("Queen's University");
INSERT INTO institution (institutionName) values ("CMC");

INSERT INTO rateType (rateName, rateAmount) values ("Academic", "Academic Machine Dependant");
INSERT INTO rateType (rateName, rateAmount) values ("Industrial", "Industrial Machine Dependant");

INSERT INTO machines(machine, name, inUse, academicRate, industrialRate) VALUES('98:01:a7:8f:00:99', 'Oxford Lasers Micromachining Laser', '0',66.99, 99.25);
INSERT INTO machines(machine, name, inUse, academicRate, industrialRate) VALUES('b8:27:eb:61:98:05', 'Raith Pioneer Electron-beam', '0', 6, 99);
INSERT INTO machines(machine, name, inUse, academicRate, industrialRate) VALUES('00:00:00:00:00:03', 'NxQ 4006 Mask Aligner', '0',6, 99);
INSERT INTO machines(machine, name, inUse, academicRate, industrialRate) VALUES('00:00:00:00:00:04', 'IMP SF-100 Xpress Maskless Photolithography System','0', 6, 99);
INSERT INTO machines(machine, name, inUse, academicRate, industrialRate) VALUES('00:00:00:00:00:05', 'Trion MiniLock III Reactive Ion Etcher', '0', 6, 99);
INSERT INTO machines(machine, name, inUse, academicRate, industrialRate) VALUES('00:00:00:00:00:06', 'PVD 75 Sputtering System','0',66, 99);
INSERT INTO machines(machine, name, inUse, academicRate, industrialRate) VALUES('00:00:00:00:00:07', 'Thermionics electron-beam Evaporator', '0', 66, 99);
