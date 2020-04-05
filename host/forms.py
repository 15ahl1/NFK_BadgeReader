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
    MachineMacAddress = StringField('Mac Address', validators=[DataRequired("This field is reqired and must be a valid MAC Address e.g. 98:01:a7:8f:00:99"), MacAddress()])
    academicAmount = DecimalField('Academic Rate', validators=[DataRequired("This field is reqired and must be a number"), NumberRange(min=0, max=10000000)])
    industrialAmount = DecimalField('Industrial Rate', validators=[DataRequired("This field is reqired and must be a number"), NumberRange(min=0, max=10000000)])
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
    perMac1 = BooleanField('Machine 1')
    perMac2 = BooleanField('Machine 2')
    perMac3 = BooleanField('Machine 3')
    perMac4 = BooleanField('Machine 4')
    perMac5 = BooleanField('Machine 5')
    perMac6 = BooleanField('Machine 6')
    perMac7 = BooleanField('Machine 7')
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
