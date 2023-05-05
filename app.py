from flask import Flask, render_template, request, redirect
import cx_Oracle

app = Flask(__name__)

DB_USER = "system"
DB_PASSWORD = "india1234"
HOST = "localhost"
PORT = 1521
DNS = "XE"


def getConnection():
    connection = cx_Oracle.connect("{DB_USER}/{DB_PASSWORD}@{HOST}:{PORT}/XE")
    return connection


@app.route("/")
def helloworld():
    return render_template("base.html")


@app.route("/addcourse")
def addcourse():
    return render_template("add_course.html")


@app.route("/managecourse")
def managecourse():
    return render_template("manage_course.html")


@app.route("/managebatch")
def managebatch():
    return render_template("manage_batch.html")


@app.route("/managestaff")
def managestaff():
    return render_template("manage_staff.html")


@app.route("/staffattendance")
def staffattendace():
    return render_template("staff_attendance.html")


@app.route("/staffsalary")
def staffsalary():
    return render_template("staff_salary.html")


@app.route("/managestudent")
def managestudent():
    return render_template("manage_student.html")


@app.route("/trialstudent")
def trialstudent():
    return render_template("trial_student.html")


@app.route("/studentattendace")
def studentattendace():
    return render_template("student_attendace.html")


@app.route("/passoutstudent")
def passoutstudent():
    return render_template("passout_student.html")


@app.route("/enquiry")
def enquiry():
    return render_template("enquiry.html")


@app.route("/feemanagement")
def feemanagement():
    return render_template("fee_manage.html")


@app.route("/expensemanage")
def expensemanage():
    return render_template("manage_expense.html")


@app.route("/feereport")
def feereport():
    return render_template("fee_report.html")


@app.route("/gstreport")
def gstreport():
    return render_template("gst_report.html")


@app.route("/expensereport")
def expensereport():
    return render_template("expense_report.html")


@app.route("/studentreport")
def studentreport():
    return render_template("student_report.html")


@app.route("/allsms")
def allsms():
    return render_template("all_sms.html")


@app.route("/studentsms")
def allsms():
    return render_template("stud_sms.html")


@app.route("/staffsms")
def allsms():
    return render_template("staff_sms.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
