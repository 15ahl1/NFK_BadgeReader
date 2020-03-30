CREATE TABLE users(
  userID int not null auto_increment,
  username varchar(50),
  supervisor varchar(50),
  department varchar(50),
  faculty varchar(50),
  institution varchar(50),
  rateType int,
  Permissions varchar(7),
  PRIMARY KEY (userID)
);


CREATE TABLE entries(
  machine varchar(50),
  timeUsed datetime,
  userID varchar(50),
  inUse boolean
);

CREATE TABLE machines(
  machine varchar(50),
  inUse boolean
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
  rateAmount int,
  PRIMARY KEY (rateID)
);

INSERT INTO machines(machine, inUse) VALUES('98:01:a7:8f:00:99', '0');
INSERT INTO machines(machine, inUse) VALUES('b8:27:eb:61:98:05', '0');
INSERT INTO machines(machine, inUse) VALUES('00:00:00:00:00:03', '0');
INSERT INTO machines(machine, inUse) VALUES('00:00:00:00:00:04', '0');
INSERT INTO machines(machine, inUse) VALUES('00:00:00:00:00:05', '0');
INSERT INTO machines(machine, inUse) VALUES('00:00:00:00:00:06', '0');
INSERT INTO machines(machine, inUse) VALUES('00:00:00:00:00:07', '0');

INSERT INTO `users` (`username`, `supervisor`, `department`, `faculty`, `institution`, `rateType`, `Permissions`) VALUES ('michael', 'bob', 'computer science', 'cs', 'queens', '33', '1010101');


INSERT INTO `supervisors` (`superName`) VALUES ('Graham Gibson');
INSERT INTO `departments` (`deptName`) VALUES ('Queen\'s University');
INSERT INTO `departments` (`deptName`) VALUES ('st lawrence');
INSERT INTO `faculty` (`facultyName`) VALUES ('CMC');
INSERT INTO `institution` (`institutionName`) VALUES ('CMC');
INSERT INTO `rateType` (`ratename`, `rateAmount`) VALUES ('Regular Usage', 22);
INSERT INTO `rateType` (`ratename`, `rateAmount`) VALUES ('Service Project', 33);
