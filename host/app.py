from flask import Flask, render_template, url_for, flash, redirect, request
from flask_wtf import FlaskForm
from forms import *
from flask_mysqldb import MySQL
import yaml
import json
import os
import io
import datetime
import pandas
import html
import decimal

app = Flask(__name__)

# Configure db
db = yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['SECRET_KEY'] = os.urandom(24)
app.config['MYSQL_DB'] = db['mysql_db']
mysql = MySQL(app)

uploads_dir = os.path.join(app.instance_path, 'uploads')

# All routing
@app.route('/')
def index():
    return home()


@app.route('/home.html', methods=['GET', 'POST',  'PUT'])
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM machines")
    machines = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template("/home.html", machines=machines)


@app.route('/time.html', methods=['GET', 'POST',  'PUT'])
def timeFunction():
    # form = userTime()
    default_name = ''
    name = request.args.get('userName', default_name)
    default_date = ''
    date = request.args.get('date', default_date)
    default_machine = ''
    machine = request.args.get('machineNumber', default_machine)
    return timeHelper(name, date, machine)


def timeHelper(name, date, machine):
    value1 = 0
    value2 = 0
    value3 = 0
    value4 = 0
    value5 = 0
    value6 = 0
    value7 = 0
    units = "Number of Hours of Machine Use For All Users"
    errorMessage = ""

    # Get Machines
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM machines")
    machines = cur.fetchall()
    mysql.connection.commit()
    cur.close()

    if name != '':
        units = "Number of Hours of Machine Use For " + name
        currentDate = datetime.date.today()
        yesterday = currentDate - datetime.timedelta(days=1)
        twoDays = currentDate - datetime.timedelta(days=2)
        threeDays = currentDate - datetime.timedelta(days=3)
        fourDays = currentDate - datetime.timedelta(days=4)
        fiveDays = currentDate - datetime.timedelta(days=5)
        sixDays = currentDate - datetime.timedelta(days=6)
        label1 = sixDays.strftime("%A") + " " + str(sixDays.day)
        label2 = fiveDays.strftime("%A") + " " + str(fiveDays.day)
        label3 = fourDays.strftime("%A") + " " + str(fourDays.day)
        label4 = threeDays.strftime("%A") + " " + str(threeDays.day)
        label5 = twoDays.strftime("%A") + " " + str(twoDays.day)
        label6 = yesterday.strftime("%A") + " " + str(yesterday.day)
        label7 = currentDate.strftime("%A") + " " + str(currentDate.day)

        cur = mysql.connection.cursor()
        userID = cur.execute("SELECT userID FROM users WHERE userName = (%s)", ([name]))
        length = cur.execute("SELECT timeUsed FROM entries WHERE userID = (%s)", ([userID]))
        usage = cur.fetchall()
        mysql.connection.commit()
        cur.close()
        if length == 0:
            errorMessage = "No values for that user"
        else:
            if length % 2 != 0:
                length -= 1
            for i in range(0, length, 2):
                sessionTime = usage[i+1][0] - usage[i][0]
                sessionTime = sessionTime.total_seconds() / 3600
                if usage[i][0].date() == currentDate:
                    value7 += sessionTime
                elif usage[i][0].date() == yesterday:
                    value6 += sessionTime
                elif usage[i][0].date() == twoDays:
                    value5 += sessionTime
                elif usage[i][0].date() == threeDays:
                    value4 += sessionTime
                elif usage[i][0].date() == fourDays:
                    value3 += sessionTime
                elif usage[i][0].date() == fiveDays:
                    value2 += sessionTime
                elif usage[i][0].date() == sixDays:
                    value1 += sessionTime
    elif date != '':
        labels = ["","","","","","",""]
        for i in range(len(machines)):
            labels[i] = machines[i][1]

        label1 = labels[0]
        label2 = labels[1]
        label3 = labels[2]
        label4 = labels[3]
        label5 = labels[4]
        label6 = labels[5]
        label7 = labels[6]
        units = "Number of Hours of Machine Use For " + date

        cur = mysql.connection.cursor()
        if len(date) != 10:
            errorMessage = "No entries this week for that date"
        else:
            #01/01/2020 <example>
            dateQuery = date[6:10] + "-" + date[0: 2] + "-" + date[3:5]
            length = cur.execute("SELECT timeUsed, machine FROM entries WHERE DATE(timeUsed) = (%s)", ([dateQuery]))
            usage = cur.fetchall()
            mysql.connection.commit()
            cur.close()
            if length == 0:
                errorMessage = "No entries for that date"
            else:
                if length % 2 != 0:
                    length -= 1
                for i in range(0, length, 2):
                    sessionTime = usage[i+1][0] - usage[i][0]
                    sessionTime = sessionTime.total_seconds() / 3600

                    for machine in machines:
                        if usage[i][1] == machine[0]:
                            value1 += sessionTime
                        elif usage[i][1] == machine[0]:
                            value2 += sessionTime
                        elif usage[i][1] == machine[0]:
                            value3 += sessionTime
                        elif usage[i][1] == machine[0]:
                            value4 += sessionTime
                        elif usage[i][1] == machine[0]:
                            value5 += sessionTime
                        elif usage[i][1] == machine[0]:
                            value6 += sessionTime
                        elif usage[i][1] == machine[0]:
                            value7 += sessionTime

    elif machine != '':
        # Get Selected Machine by mac
        selected_mac = html.unescape(machine)
        # Get Machines Name
        cur = mysql.connection.cursor()
        cur.execute("SELECT name from machines WHERE machine = '{}'".format(selected_mac))
        name = cur.fetchone()
        mysql.connection.commit()
        cur.close()


        units = "Number of Hours of Machine Use For: " + name[0]
        currentDate = datetime.date.today()
        yesterday = currentDate - datetime.timedelta(days=1)
        twoDays = currentDate - datetime.timedelta(days=2)
        threeDays = currentDate - datetime.timedelta(days=3)
        fourDays = currentDate - datetime.timedelta(days=4)
        fiveDays = currentDate - datetime.timedelta(days=5)
        sixDays = currentDate - datetime.timedelta(days=6)
        label1 = sixDays.strftime("%A") + " " + str(sixDays.day)
        label2 = fiveDays.strftime("%A") + " " + str(fiveDays.day)
        label3 = fourDays.strftime("%A") + " " + str(fourDays.day)
        label4 = threeDays.strftime("%A") + " " + str(threeDays.day)
        label5 = twoDays.strftime("%A") + " " + str(twoDays.day)
        label6 = yesterday.strftime("%A") + " " + str(yesterday.day)
        label7 = currentDate.strftime("%A") + " " + str(currentDate.day)

        cur = mysql.connection.cursor()
        length = cur.execute("SELECT timeUsed FROM entries WHERE machine = '{}'".format(selected_mac))
        usage = cur.fetchall()
        mysql.connection.commit()
        cur.close()
        if length == 0:
            errorMessage = "No entries this week for that machine"
        else:
            if length % 2 != 0:
                length -= 1
            for i in range(0, length, 2):
                sessionTime = usage[i+1][0] - usage[i][0]
                sessionTime = sessionTime.total_seconds() / 3600
                if usage[i][0].date() == currentDate:
                    value7 += sessionTime
                elif usage[i][0].date() == yesterday:
                    value6 += sessionTime
                elif usage[i][0].date() == twoDays:
                    value5 += sessionTime
                elif usage[i][0].date() == threeDays:
                    value4 += sessionTime
                elif usage[i][0].date() == fourDays:
                    value3 += sessionTime
                elif usage[i][0].date() == fiveDays:
                    value2 += sessionTime
                elif usage[i][0].date() == sixDays:
                    value1 += sessionTime

    else:
        currentDate = datetime.date.today()
        yesterday = currentDate - datetime.timedelta(days=1)
        twoDays = currentDate - datetime.timedelta(days=2)
        threeDays = currentDate - datetime.timedelta(days=3)
        fourDays = currentDate - datetime.timedelta(days=4)
        fiveDays = currentDate - datetime.timedelta(days=5)
        sixDays = currentDate - datetime.timedelta(days=6)
        label1 = sixDays.strftime("%A") + " " + str(sixDays.day)
        label2 = fiveDays.strftime("%A") + " " + str(fiveDays.day)
        label3 = fourDays.strftime("%A") + " " + str(fourDays.day)
        label4 = threeDays.strftime("%A") + " " + str(threeDays.day)
        label5 = twoDays.strftime("%A") + " " + str(twoDays.day)
        label6 = yesterday.strftime("%A") + " " + str(yesterday.day)
        label7 = currentDate.strftime("%A") + " " + str(currentDate.day)


        cur = mysql.connection.cursor()
        length = cur.execute("SELECT timeUsed FROM entries")
        usage = cur.fetchall()
        mysql.connection.commit()
        cur.close()
        if length == 0:
            errorMessage = "No entries this week"
        else:
            if length % 2 != 0:
                length -= 1
            for i in range(0, length, 2):
                sessionTime = usage[i+1][0] - usage[i][0]
                sessionTime = sessionTime.total_seconds() / 3600
                if usage[i][0].date() == currentDate:
                    value7 += sessionTime
                elif usage[i][0].date() == yesterday:
                    value6 += sessionTime
                elif usage[i][0].date() == twoDays:
                    value5 += sessionTime
                elif usage[i][0].date() == threeDays:
                    value4 += sessionTime
                elif usage[i][0].date() == fourDays:
                    value3 += sessionTime
                elif usage[i][0].date() == fiveDays:
                    value2 += sessionTime
                elif usage[i][0].date() == sixDays:
                    value1 += sessionTime

    return render_template('time.html', units=units, label1=label1, label2=label2, label3=label3, label4=label4, label5=label5, label6=label6, label7=label7, value1=value1, value2=value2, value3=value3, value4=value4, value5=value5, value6=value6, value7=value7, machines=machines, errorMessage=errorMessage)

@app.route('/addUser.html', methods=['GET', 'POST',  'PUT'])
def userFunction():
    form = makeNewUser()
    cur = mysql.connection.cursor()
    supers = cur.execute("SELECT superName, superName FROM supervisors")
    supers = cur.fetchall()
    dept = cur.execute("SELECT deptName, deptName FROM departments")
    dept = cur.fetchall()
    faculty = cur.execute("SELECT facultyName, facultyName FROM faculty")
    faculty = cur.fetchall()
    institution = cur.execute(
        "SELECT institutionName, institutionName FROM institution")
    institution = cur.fetchall()
    rate = cur.execute("SELECT rateAmount, rateName FROM rateType")
    rate = cur.fetchall()
    form.supervisor.choices = supers
    form.department.choices = dept
    form.faculty.choices = faculty
    form.institution.choices = institution
    form.rateType.choices = rate
    if request.method == "POST":
        permissionString = ""
        if(form.perMac1.data == True):
            permissionString += "1"
        else:
            permissionString += "0"

        if(form.perMac2.data == True):
            permissionString += "1"
        else:
            permissionString += "0"

        if(form.perMac3.data == True):
            permissionString += "1"
        else:
            permissionString += "0"

        if(form.perMac4.data == True):
            permissionString += "1"
        else:
            permissionString += "0"

        if(form.perMac5.data == True):
            permissionString += "1"
        else:
            permissionString += "0"

        if(form.perMac6.data == True):
            permissionString += "1"
        else:
            permissionString += "0"

        if(form.perMac7.data == True):
            permissionString += "1"
        else:
            permissionString += "0"
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(username, userPin, supervisor, department, faculty, institution, rateType, Permissions) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", ([form.userName.data, form.userPin.data, form.supervisor.data, form.department.data, form.faculty.data, form.institution.data, form.rateType.data, permissionString]))
        mysql.connection.commit()
        cur.close()
        return redirect('addUser.html')
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM users")
    userDetails = cur.fetchall()
    return render_template('addUser.html', form=form, userDetails=userDetails)


@app.route('/configure.html', methods=['GET', 'POST',  'PUT'])
def configure():
    superForm = newSupervisor()
    deptForm = newDepartment()
    facultyForm = newFaculty()
    institutionForm = newInstitution()
    rateForm = newRateType()
    if request.method == "POST":
        try:
            request.form['superName']
            cur = mysql.connection.cursor()
            superName = superForm.superName.data
            cur.execute(
                "INSERT INTO supervisors (superName) VALUES (%s)", ([superName]))
            mysql.connection.commit()
            cur.close()
            return redirect("/configure.html")
        except:
            pass
        try:
            request.form['deptName']
            cur = mysql.connection.cursor()
            deptName = deptForm.deptName.data
            cur.execute(
                "INSERT INTO departments (deptName) VALUES (%s)", ([deptName]))
            mysql.connection.commit()
            cur.close()
            return redirect("/configure.html")
        except:
            pass
        try:
            request.form['facultyName']
            cur = mysql.connection.cursor()
            facultyName = facultyForm.facultyName.data
            cur.execute(
                "INSERT INTO faculty (facultyName) VALUES (%s)", ([facultyName]))
            mysql.connection.commit()
            cur.close()
            return redirect("/configure.html")
        except:
            pass
        try:
            request.form['institutionName']
            cur = mysql.connection.cursor()
            institutionName = institutionForm.institutionName.data
            cur.execute(
                "INSERT INTO institution (institutionName) VALUES (%s)", ([institutionName]))
            mysql.connection.commit()
            cur.close()
            return redirect("/configure.html")
        except:
            pass
        try:
            request.form['rateTypeName']
            cur = mysql.connection.cursor()
            rateTypeName = rateForm.rateTypeName.data
            rateAmount = rateForm.rateAmount.data
            if str(rateAmount)=="None":
                cur.execute("INSERT INTO rateType (rateName, rateAmount) VALUES (%s, %s)", ([rateTypeName, str(rateTypeName)+" Machine Dependant"]))
                mysql.connection.commit()
                cur.close()
            else:
                cur.execute("INSERT INTO rateType (rateName, rateAmount) VALUES (%s, %s)", ([
                            rateTypeName, rateAmount]))
                mysql.connection.commit()
                cur.close()
            return redirect("/configure.html")
        except:
            pass
    cur = mysql.connection.cursor()
    supers = cur.execute("SELECT * FROM supervisors")
    supers = cur.fetchall()
    dept = cur.execute("SELECT * FROM departments")
    dept = cur.fetchall()
    faculty = cur.execute("SELECT * FROM faculty")
    faculty = cur.fetchall()
    institution = cur.execute("SELECT * FROM institution")
    institution = cur.fetchall()
    rate = cur.execute("SELECT * FROM rateType")
    rate = cur.fetchall()
    return render_template("/configure.html",
    supers=supers, dept=dept, faculty=faculty, institution=institution,
    rate=rate,superForm=superForm, deptForm=deptForm, facultyForm=facultyForm,
    institutionForm=institutionForm, rateForm=rateForm)




@app.route('/addMachine.html', methods=['GET', 'POST',  'PUT'])
def machineFunction():
    form = makeNewMachine()
    cur = mysql.connection.cursor()
    machines = cur.execute("SELECT * FROM machines")
    machines = cur.fetchall()
    message=""
    if form.validate_on_submit():
        message = "New Machine Made"
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO machines(machine, name, inUse,  academicRate, institutionalRate) VALUES (%s, %s, %s,%s, %s)", ([form.MachineMacAddress.data,form.MachineName.data, 0, form.academicAmount.data, form.industrialAmount.data]))
        mysql.connection.commit()
        cur.close()
        cur = mysql.connection.cursor()
        machines = cur.execute("SELECT * FROM machines")
        machines = cur.fetchall()
        return render_template("/addMachine.html", message=message, machines=machines, form=form)
    return render_template("/addMachine.html", machines=machines, form=form)



@app.route('/editMachine/<string:machineID>', methods=['GET', 'POST'])
def editMachine(machineID):
    cur = mysql.connection.cursor()
    machines = cur.execute("SELECT * FROM machines")
    machines = cur.fetchall()
    Editform = makeNewMachine()
    editMachine = cur.execute("SELECT machine, name, academicRate, institutionalRate FROM machines WHERE machineID=\"" + str(machineID) + "\"")
    editMachine = cur.fetchall()
    cur.close()
    Editform.MachineName.data = editMachine[0][1]
    Editform.MachineMacAddress.data = editMachine[0][0]
    Editform.academicAmount.data = editMachine[0][2]
    Editform.industrialAmount.data = editMachine[0][3]
    if request.method == "POST":
        print("Hello from the endi tmaching posting " + request.form.get("industrialAmount"))
        cur = mysql.connection.cursor()
        select_stmt = "UPDATE machines SET machine = %(machine)s, name = %(name)s, academicRate = %(academicRate)s, institutionalRate = %(institutionalRate)s WHERE machineID= %(machineID)s;"
        cur.execute(select_stmt, {'machine': request.form.get("MachineMacAddress"), 'name': request.form.get("MachineName"), 'academicRate':request.form.get("academicAmount"), 'institutionalRate': request.form.get("industrialAmount"), 'machineID': str(machineID)})
        mysql.connection.commit()
        return redirect("/addMachine.html")
    return render_template("/addMachine.html", machines=machines, form=Editform)




@app.route('/reports.html', methods=['GET', 'POST',  'PUT'])
def reportFunction():
    cur = mysql.connection.cursor()
    supers = cur.execute("SELECT * FROM supervisors")
    supers = cur.fetchall()
    dept = cur.execute("SELECT * FROM departments")
    dept = cur.fetchall()
    faculty = cur.execute("SELECT * FROM faculty")
    faculty = cur.fetchall()
    institution = cur.execute("SELECT * FROM institution")
    institution = cur.fetchall()
    rate = cur.execute("SELECT * FROM rateType")
    rate = cur.fetchall()
    return render_template("/reports.html",
    supers=supers, dept=dept, faculty=faculty, institution=institution, rate=rate)


@app.route('/editUser/<userID>', methods=['GET', 'POST',  'PUT'])
@app.route('/editUser.html', methods=['GET', 'POST',  'PUT'])
def editUserFunction(userID = None):
    form = editCurrentUser()
    cur = mysql.connection.cursor()
    users = cur.execute("SELECT userID, username FROM users ORDER BY username")
    users = cur.fetchall()
    form.userName.choices = users
    if request.method == "POST":
        info = request.form['userName']
        hello = "yo what up"
        return render_template("/editUser.html", form=form, data=info,hello=hello)
    if userID:
        info = userID
        hello = "yo what up"
        return render_template("/editUser.html", form=form, data=info,hello=hello)
    return render_template("/editUser.html", form=form)


@app.route('/reportUsage.html', methods=['GET', 'POST',  'PUT'])
def reportUsageFunction():
    cur = mysql.connection.cursor()
    sessions = cur.execute("SELECT * FROM sessions")
    sessions = cur.fetchall()
    return render_template("/reportUsage.html", sessions=sessions)



# All report upload to database files
@app.route("/uploadSuper", methods=["POST"])
def uploadSuper():
    file = request.files['uploadSuper']
    file.save('instance/uploads/Supervisors_file.xlsx')
    answers = pandas.read_excel(file)
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM supervisors")
    for item in answers['superName']:
        cur.execute(
            "INSERT INTO supervisors (superName) VALUES (%s)", ([item]))
    mysql.connection.commit()
    cur.close()
    return redirect("/reports.html")

@app.route("/uploadDepartments", methods=["POST"])
def uploadDepartments():
    file = request.files['uploadDepartments']
    file.save('instance/uploads/Departments_file.xlsx')
    answers = pandas.read_excel(file)
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM departments")
    for item in answers['deptName']:
        cur.execute(
            "INSERT INTO departments (deptName) VALUES (%s)", ([item]))
    mysql.connection.commit()
    cur.close()
    return redirect("/reports.html")

@app.route("/uploadFaculty", methods=["POST"])
def uploadFaculty():
    file = request.files['uploadFaculty']
    file.save('instance/uploads/Faculty_file.xlsx')
    answers = pandas.read_excel(file)
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM faculty")
    for item in answers['facultyName']:
        cur.execute(
            "INSERT INTO faculty (facultyName) VALUES (%s)", ([item]))
    mysql.connection.commit()
    cur.close()
    return redirect("/reports.html")

@app.route("/uploadInstitution", methods=["POST"])
def uploadInstitution():
    file = request.files['uploadInstitution']
    file.save('instance/uploads/Institution_file.xlsx')
    answers = pandas.read_excel(file)
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM institution")
    for item in answers['institutionName']:
        cur.execute(
            "INSERT INTO institution (institutionName) VALUES (%s)", ([item]))
    mysql.connection.commit()
    cur.close()
    return redirect("/reports.html")

@app.route("/uploadRateType", methods=["POST"])
def uploadRateType():
    file = request.files['uploadRateType']
    file.save('instance/uploads/RateType_file.xlsx')
    answers = pandas.read_excel(file)
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM rateType")
    names = answers['rateName']
    rates = answers['rateAmount']
    for x in range(0,names.size-1):
        cur.execute("INSERT INTO rateType (rateName, rateAmount) VALUES (%s, %s)", ([names[x], rates[x]]))
    mysql.connection.commit()
    cur.close()
    return redirect("/reports.html")


@app.route("/uploadUsers", methods=["POST"])
def uploadUsers():
    file = request.files['uploadUsers']
    file.save('instance/uploads/Users_file.xlsx')
    answers = pandas.read_excel(file)
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM Users")
    for item1,item2 in answers['rateType']:
        cur.execute(
            "INSERT INTO rateType (rateName, rateAmount) VALUES (%s, %s)", ([item1, item2]))
    mysql.connection.commit()
    cur.close()
    return redirect("/reports.html")




# All report downloads to database files
@app.route("/downloadSuper", methods=["POST"])
def downloadSuper():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM supervisors')
    wb = Workbook()
    ws = wb.active


    pandaDataFrame = pandas.DataFrame(cur.fetchall())
    pandaDataFrame.to_excel('instance/download.Supervisors_file.xlsx')
    mysql.connection.commit()
    cur.close()
    return redirect("/reports.html")


# All functions to delete things such as users, supers, institutions
@app.route('/deleteUser/<string:userIdentificationNumber>')
def deleteUser(userIdentificationNumber):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM users where userID=" +
                str(userIdentificationNumber))
    mysql.connection.commit()
    cur.close()
    form = makeNewUser()
    return redirect("/addUser.html")


@app.route('/deleteSuper/<string:superIdentificationNumber>')
def deleteSuper(superIdentificationNumber):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM supervisors where superID=" +
                str(superIdentificationNumber))
    mysql.connection.commit()
    cur.close()
    return redirect("/configure.html")


@app.route('/deleteDepartment/<string:deptIdentificationNumber>')
def deleteDepartment(deptIdentificationNumber):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM departments where deptID=" +
                str(deptIdentificationNumber))
    mysql.connection.commit()
    cur.close()
    return redirect("/configure.html")


@app.route('/deleteFaculty/<string:facultyIdentificationNumber>')
def deleteFaculty(facultyIdentificationNumber):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM faculty where facultyID=" +
                str(facultyIdentificationNumber))
    mysql.connection.commit()
    cur.close()
    return redirect("/configure.html")


@app.route('/deleteInstitution/<string:institutionIdentificationNumber>')
def deleteInstitution(institutionIdentificationNumber):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM institution where institutionID=" +
                str(institutionIdentificationNumber))
    mysql.connection.commit()
    cur.close()
    return redirect("/configure.html")


@app.route('/deleteRate/<string:rateIdentificationNumber>')
def deleteRate(rateIdentificationNumber):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM rateType where rateID=" +
                str(rateIdentificationNumber))
    mysql.connection.commit()
    cur.close()
    return redirect("/configure.html")

@app.route('/deleteMachine/<string:MachineIdentification>')
def deleteMachine(MachineIdentification):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM machines where name=\"" + str(MachineIdentification) + "\"")
    mysql.connection.commit()
    cur.close()
    return redirect("/addMachine.html")



@app.route('/editSession/<string:SessionID>')
def editSession(SessionID):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM sessions where sessionID=\"" + str(SessionID) + "\"")
    mysql.connection.commit()
    cur.close()
    return redirect("/addMachine.html")

def writeUsageRecord(machine, time, userID):
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO entries (machine,timeUsed, userID, inUse, enteredSession) VALUES (%s, %s, %s, %s, %s);",
                    (machine, time, userID, str(1), str(0)))
        mysql.connection.commit()
        cur.close()
        cur = mysql.connection.cursor()
        select_stmt = "SELECT * FROM entries WHERE machine = %(machine)s and userID = %(userID)s and enteredSession=\'0\'"
        entries = cur.execute(select_stmt, {'machine': machine,'userID':userID })
        entries = cur.fetchall()
        if len(entries)==2:
            select_stmt = "SELECT * FROM users WHERE userPin = %(userPin)s"
            user = cur.execute(select_stmt, {'userPin':userID })
            user = cur.fetchall()

            select_stmt = "SELECT * FROM machines WHERE machine = %(machine)s"
            machineData = cur.execute(select_stmt, {'machine':machine })
            machineData = cur.fetchall()


            if user[0][7]=="Academic Machine Dependant":
                rateUsed = machineData[0][3]
            elif user[0][7]=="Institutional Machine Dependant":
                rateUsed = machineData[0][4]
            else:
                rateUsed = user[0][7]

            diff = entries[1][2] - entries[0][2]
            days, seconds = diff.days, diff.seconds
            hours = decimal.Decimal(days * 24 + seconds // 3600)
            minutes = decimal.Decimal((seconds % 3600) // 60)
            seconds = decimal.Decimal(seconds % 60)

            rateUsed = decimal.Decimal(rateUsed)
            timeUsed = str(hours) + " Hours " + str(minutes) + " Minutes " + str(seconds) + " Seconds "
            timeUSedDecimal = decimal.Decimal(hours) + (minutes/decimal.Decimal(60)) + (seconds/decimal.Decimal(3600))
            billAmount = rateUsed * hours + rateUsed * (minutes/decimal.Decimal(60)) + rateUsed * (seconds/decimal.Decimal(60*60))

            record = [machine,machineData[0][1],entries[0][2],entries[1][2],timeUsed,rateUsed,user[0][7],billAmount, userID,user[0][1]]

            # Make sessions record
            select_stmt = "INSERT INTO sessions(machineID,machineName,sessionStart,sessionEnd,timeUsed,rateUsed,rateTypeUsed,billAmount,userID,userName) VALUES(%(machineID)s,%(machineName)s,%(sessionStart)s,%(sessionEnd)s,%(timeUsed)s,%(rateUsed)s,%(rateTypeUsed)s,%(billAmount)s,%(userID)s, %(userName)s);"
            cur.execute(select_stmt, {'machineID': machine,'machineName':machineData[0][1],'sessionStart': entries[0][2],'sessionEnd':entries[1][2],'timeUsed': timeUSedDecimal,'rateUsed':rateUsed,'rateTypeUsed': user[0][7],'billAmount':billAmount,'userID': userID,'userName':user[0][1]})
            mysql.connection.commit()
            cur.close()

            # Update entries table to show that the entries have been moved over to the sessions table
            cur = mysql.connection.cursor()
            select_stmt = "update entries set enteredSession=1 where entrieID= %(entrieID)s;"
            cur.execute(select_stmt, {'entrieID': entries[0][0]})
            mysql.connection.commit()
            select_stmt = "update entries set enteredSession=1 where entrieID= %(entrieID)s;"
            cur.execute(select_stmt, {'entrieID': entries[1][0]})
            mysql.connection.commit()
            cur.close()





def machineStatus(machine):
    print("Updating machine status...")
    with app.app_context():
        cur = mysql.connection.cursor()
        select_stmt = "SELECT inUse FROM machines WHERE machine = %(machine)s"
        cur.execute(select_stmt, {'machine': machine})
        status = cur.fetchone()
        print(status)
        print("The machine status is " + str(status[0]))
        if status[0] == 0:
            update_stmt = "UPDATE machines SET inUse = '1' WHERE machine = %(machine)s"
            cur.execute(update_stmt, {'machine': machine})
        else:
            update_stmt = "UPDATE machines SET inUse = '0' WHERE machine = %(machine)s"
            cur.execute(update_stmt, {'machine': machine})
        mysql.connection.commit()
        cur.close()
