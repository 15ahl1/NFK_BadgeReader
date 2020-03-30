from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, FormField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_mysqldb import MySQL
import yaml
from app import *

class userTime(FlaskForm):
    userName = StringField('Username', validators=[DataRequired(), Length(min=2,max=20)])
    submit = SubmitField("Submit")


class makeNewUser(FlaskForm):
    userName = StringField('username', validators=[DataRequired(), Length(min=2,max=20)])
    supervisor = SelectField(
        'Supervisor',
        choices=[('Queens University','Queens University')]
    )
    department = SelectField(
        'Department',
        choices=[('Queens University','Queens University'), ('SUPER2', 'SUPER2'), ('SUPER3', 'SUPER3')]
    )
    faculty = SelectField(
        'Faculty',
        choices=[('Queens University','Queens University'), ('SUPER2', 'SUPER2'), ('SUPER3', 'SUPER3')]
    )
    institution = SelectField(
        'Institution',
        choices=[('Queens University','Queens University'), ('SUPER2', 'SUPER2'), ('SUPER3', 'SUPER3')]
    )
    rateType = SelectField(
        'Rate Type',
        choices=[('Academic', 'Academic'), ('Industrial', 'Industrial')]
    )

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
    rateAmount = StringField('Rate Amount', validators=[DataRequired(), Length(min=2,max=20)])
    submit = SubmitField("Submit")
