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


CREATE TABLE entries(
  entrieID int not null auto_increment PRIMARY KEY,
  machine varchar(50),
  timeUsed datetime,
  userID varchar(50),
  inUse boolean,
  enteredSession boolean
);



CREATE TABLE machines(
  machine varchar(50),
  name varchar(100),
  inUse boolean,
  academicRate decimal,
  institutionalRate decimal,
  machineID int not null auto_increment PRIMARY KEY
);

CREATE TABLE machine1 (
  userID int);

CREATE TABLE machine2 (
  userID int);

CREATE TABLE machine3 (
  userID int);

CREATE TABLE machine4 (
  userID int);

CREATE TABLE machine5 (
  userID int);

CREATE TABLE machine6 (
  userID int);

CREATE TABLE machine7 (
  userID int);

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

INSERT INTO sessions(machineID,machineName,sessionStart,sessionEnd,timeUsed,rateUsed,rateTypeUsed,billAmount,userID,userName)
VALUES("98:01:a7:8f:00:99","Oxford Lasers Micromachining Laser","2020-03-29 00:09:40","2020-03-29 00:012:40",3.45,"22","Academic",23.33,"12345", "Michael Reinhart");

INSERT INTO machines(machine, name, inUse, academicRate, institutionalRate) VALUES('98:01:a7:8f:00:99', 'Oxford Lasers Micromachining Laser', '0',66, 99);
INSERT INTO machines(machine, name, inUse, academicRate, institutionalRate) VALUES('b8:27:eb:61:98:05', 'Raith Pioneer Electron-beam', '0', 6, 99);
INSERT INTO machines(machine, name, inUse, academicRate, institutionalRate) VALUES('00:00:00:00:00:03', 'NxQ 4006 Mask Aligner', '0',6, 99);
INSERT INTO machines(machine, name, inUse, academicRate, institutionalRate) VALUES('00:00:00:00:00:04', 'IMP SF-100 Xpress Maskless Photolithography System','0', 6, 99);
INSERT INTO machines(machine, name, inUse, academicRate, institutionalRate) VALUES('00:00:00:00:00:05', 'Trion MiniLock III Reactive Ion Etcher', '0', 6, 99);
INSERT INTO machines(machine, name, inUse, academicRate, institutionalRate) VALUES('00:00:00:00:00:06', 'PVD 75 Sputtering System','0',66, 99);
INSERT INTO machines(machine, name, inUse, academicRate, institutionalRate) VALUES('00:00:00:00:00:07', 'Thermionics electron-beam Evaporator', '0', 66, 99);

INSERT INTO `users` (`username`, `supervisor`, `department`, `faculty`, `institution`, `rateType`, `Permissions`) VALUES ('michael', 'bob', 'computer science', 'cs', 'queens', '33', '1010101');


INSERT INTO `supervisors` (`superName`) VALUES ('Graham Gibson');
INSERT INTO `departments` (`deptName`) VALUES ('Queen\'s University');
INSERT INTO `departments` (`deptName`) VALUES ('st lawrence');
INSERT INTO `faculty` (`facultyName`) VALUES ('CMC');
INSERT INTO `institution` (`institutionName`) VALUES ('CMC');
INSERT INTO `rateType` (`ratename`, `rateAmount`) VALUES ('Regular Usage', "22");
INSERT INTO `rateType` (`ratename`, `rateAmount`) VALUES ('Service Project', "33");


-- Three Sessions
INSERT INTO entries(machine,timeUsed,userID,inUse,enteredSession) VALUES ('98:01:a7:8f:00:99',"2020-03-29 00:09:40","12345",1,1);
INSERT INTO entries(machine,timeUsed,userID,inUse,enteredSession) VALUES ('98:01:a7:8f:00:99',"2020-03-29 00:012:40","12345",0,1);


INSERT INTO entries(machine,timeUsed,userID,inUse,enteredSession) VALUES ('98:01:a7:8f:00:99',"2020-04-20 00:09:40","12345",1,0);
INSERT INTO entries(machine,timeUsed,userID,inUse,enteredSession) VALUES ('98:01:a7:8f:00:99',"2020-04-20 00:012:40","12345",0,0);


INSERT INTO entries(machine,timeUsed,userID,inUse,enteredSession) VALUES ('b8:27:eb:61:98:05',"2020-03-29 00:012:40","12345",1,0);
INSERT INTO entries(machine,timeUsed,userID,inUse,enteredSession) VALUES ('b8:27:eb:61:98:05',"2020-03-29 00:17:40","12345",0,0);
