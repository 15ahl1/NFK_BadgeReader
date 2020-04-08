from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, FormField, DecimalField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange, MacAddress
from flask_mysqldb import MySQL
import yaml
from app import *

class userTime(FlaskForm):
    userName = StringField('Username', validators=[DataRequired(), Length(min=2,max=20)])
    submit = SubmitField("Submit")

class makeNewMachine(FlaskForm):
    MachineName = StringField('Name', description="test", validators=[DataRequired(), Length(min=2,max=100)])
    MachineMacAddress = StringField('MAC Address', validators=[DataRequired("This field is required and must be a valid MAC Address e.g. 98:01:a7:8f:00:99"), MacAddress()])
    academicAmount = DecimalField('Academic Rate', validators=[DataRequired("This field is required and must be a number"), NumberRange(min=0, max=10000000)])
    industrialAmount = DecimalField('Industrial Rate', validators=[DataRequired("This field is required and must be a number"), NumberRange(min=0, max=10000000)])
    submit = SubmitField("Submit")

class editCurrentUser(FlaskForm):
    userName = SelectField('Select User to Edit')
    submit = SubmitField("Submit")


class makeNewUser(FlaskForm):
    userName = StringField('Username', validators=[DataRequired(), Length(min=2,max=40)])
    userPin = StringField('Card Number', validators=[DataRequired(), Length(min=2,max=100)])
    supervisor = SelectField('Supervisor')
    department = SelectField('Department',)
    faculty = SelectField('Faculty')
    institution = SelectField('Institution')
    rateType = SelectField('Rate Type')
    perMac1 = BooleanField('Oxford Lasers Micromachining Laser')
    perMac2 = BooleanField('Raith Pioneer Electron-beam')
    perMac3 = BooleanField('NxQ 4006 Mask Aligner')
    perMac4 = BooleanField('IMP SF-100 Xpress Maskless Photolithography System')
    perMac5 = BooleanField('Trion MiniLock III Reactive Ion Etcher')
    perMac6 = BooleanField('PVD 75 Sputtering System')
    perMac7 = BooleanField('Thermionics electron-beam Evaporator')
    submit = SubmitField("Submit")

class editSessionData(FlaskForm):
    machineMacAddress = StringField('Mac Address', validators=[DataRequired("This field is required and must be a valid MAC Address e.g. 98:01:a7:8f:00:99"), MacAddress()])
    machineName = StringField('Machine Name', validators=[DataRequired(), Length(min=2,max=40)])
    sessionStart = StringField('Session Start', validators=[DataRequired(), Length(min=2,max=40)])
    sessionEnd = StringField('Session End', validators=[DataRequired(), Length(min=2,max=40)])
    timeUsed = DecimalField('Time Used', validators=[DataRequired("This field is required and must be a number"), NumberRange(min=0, max=10000000)])
    rateUsed = DecimalField('Rate Used', validators=[DataRequired("This field is required and must be a number"), NumberRange(min=0, max=10000000)])
    billAmount = DecimalField('Bill Amount', validators=[DataRequired("This field is required and must be a number"), NumberRange(min=0, max=10000000)])
    rateTypeUsed = StringField('Type of rate', validators=[DataRequired(), Length(min=2,max=40)])
    userID = StringField('userID', validators=[DataRequired(), Length(min=2,max=40)])
    UserName = StringField('Username', validators=[DataRequired(), Length(min=2,max=40)])
    submit = SubmitField("Submit")


class newSupervisor(FlaskForm):
    superName = StringField('Supervisor Name', validators=[DataRequired(), Length(min=2,max=20)])
    submit = SubmitField("Submit")

class newDepartment(FlaskForm):
    deptName = StringField('Department Name', validators=[DataRequired(), Length(min=2,max=20)])
    submit = SubmitField("Submit")

class newFaculty(FlaskForm):
    facultyName = StringField('Faculty Name', validators=[DataRequired(), Length(min=2,max=20)])
    submit = SubmitField("Submit")

class newInstitution(FlaskForm):
    institutionName = StringField('Institution Name', validators=[DataRequired(), Length(min=2,max=20)])
    submit = SubmitField("Submit")

class newRateType(FlaskForm):
    rateTypeName = StringField('Rate Name', validators=[DataRequired(), Length(min=2,max=20)])
    rateAmount = DecimalField('Rate Amount')
    submit = SubmitField("Submit")
