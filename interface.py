import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import QSqlQueryModel,QSqlDatabase,QSqlQuery
from PyQt4.QtGui import QTableView,QApplication
from PyQt4 import QtSql,QtGui
from PyQt4 import QtGui, QtCore
import pypyodbc


def window():
    win = QWidget()
    b1 = QPushButton("View Data")
    b2 = QPushButton("Modify Data")
    b5 = QPushButton("SIRIUS CONTACTOR SO/SOO")
    win.setWindowIcon(QIcon('Blue.ico'))
    vbox = QVBoxLayout()
    hbox = QHBoxLayout()
    hbox.addWidget(b1)
    hbox.addStretch()
    hbox.addWidget(b2)
    vbox.addWidget(b5)
    vbox.addStretch()
    vbox.addLayout(hbox)
    win.setLayout(vbox)
    win.setWindowTitle("Troubleshooting")
    win.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #ffffff); padding: 50px; font: 17px; border-width: 2px;")
    b1.setMinimumHeight(100)
    b1.setMinimumWidth(100)
    b2.setMinimumHeight(100)
    b2.setMinimumWidth(100)
    b5.setMaximumHeight(35)
    b5.setFlat(True)
    b1.setFont(QFont('Candara',10))
    b2.setFont(QFont('Candara',10))
    b5.setFont(QFont('Candara',10))
    b5.setStyleSheet("color: #0a3a2a;")
    b1.setStyleSheet("color: #0a3a2a; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); border-style:outset; border-width: 2px; border-radius: 10px; border-color: beige;")
    b2.setStyleSheet(
        "color: #0a3a2a; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); border-style:outset; border-width: 2px; border-radius: 10px; border-color: beige;")


    icon1 = QIcon("Capture.PNG")
    # icon2 = QIcon("viewData.PNG")
    # icon3 = QIcon("modifyData.PNG")
    b5.setIconSize(QSize(100, 30))
    b5.setIcon(icon1)
    # b1.setIconSize(QSize(180,250))
    # b1.setIcon(icon2)
    # b2.setIconSize(QSize(180,250))
    # b2.setIcon(icon3)
    b1.clicked.connect(view_data)
    b2.clicked.connect(login_box)
    win.show()
    sys.exit(app.exec_())


def view_data():
    w = QWidget()
    b0 = QPushButton("Select Area:")
    b1 = QPushButton("Select Sub Area:")
    b2 = QPushButton("Select Station ID/Workstation:")
    b3 = QPushButton("")
    b4 = QPushButton("Submit")
    w.setWindowIcon(QIcon('Blue.ico'))
    w.setWindowTitle("View Data")
    b0.setFlat(True)
    b1.setFlat(True)
    b2.setFlat(True)
    b3.setFlat(True)
    w.setStyleSheet("background-color:background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #ffffff); padding: 5px; font: 20px; border-width: 2px; Text-align: left;")
    w.resize(700, 100)
    b0.setFont(QFont('Candara',12))
    b0.setStyleSheet("color: #0a3a2a; Text-align: left; background-color: white")
    b1.setFont(QFont('Candara',12))
    b1.setStyleSheet("color: #0a3a2a; Text-align: left;")
    b2.setFont(QFont('Candara',12))
    b2.setStyleSheet("color: #0a3a2a; Text-align: left;")
    b4.setFont(QFont('Candara',12))
    hbox = QHBoxLayout()
    vbox = QVBoxLayout()
    global cb0
    global cb1
    global cb2
    cb0 = QComboBox()
    cb1 = QComboBox()
    cb2 = QComboBox()
    cb0.setStyleSheet("border-radius: 3px; border: 1px beige; font: 15px; padding: 3px; font-family: Candara;")
    cb1.setStyleSheet("border-radius: 3px; border: 1px beige; font: 15px; padding 3px; font-family: Candara;")
    cb2.setStyleSheet("border-radius: 3px; border: 1px beige; font: 15px; padding 3px; font-family: Candara;")
    b4.setStyleSheet(
        "color: #0a3a2a; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); border-style:outset; border-width: 2px; border-radius: 5px; border-color: beige; padding: 2px;")

    vbox.addWidget(b0)
    vbox.addStretch()
    vbox.addWidget(cb0)
    vbox.addWidget(b1)
    vbox.addStretch()
    vbox.addWidget(cb1)
    vbox.addWidget(b2)
    vbox.addStretch()
    vbox.addWidget(cb2)
    vbox.addStretch()
    vbox.addWidget(b3)
    vbox.addWidget(b4)

    cb0.addItem("Pre Manufacturing")
    cb0.addItem("Assembly Area")
    cb0.addItem("Coil Winding")

    cb1.addItem("Plastic Shop")
    cb1.addItem("Metal Shop")
    cb1.addItem("A1")
    cb1.addItem("A2")
    cb1.addItem("A3/A4")
    cb1.addItem("A5/A6")
    cb1.addItem("A13")
    cb1.addItem("Packing")
    cb1.addItem("Repair")
    cb1.addItem("Winding")
    cb1.addItem("Marsili Automation")

    cb2.addItem("NA")
    cb2.addItem("M00")
    cb2.addItem("M10")
    cb2.addItem("M20")
    cb2.addItem("M30")
    cb2.addItem("M40")
    cb2.addItem("M50")
    cb2.addItem("M60")
    cb2.addItem("M70")
    cb2.addItem("M80")
    cb2.addItem("M90")
    cb2.addItem("M100")
    cb2.addItem("M110")
    cb2.addItem("M120")

    b4.clicked.connect(submit)
    vbox.addLayout(hbox)
    w.setLayout(vbox)
    w.show()
    w.exe_()


def submit():
    if cb0.currentText() == 'Assembly Area' and cb1.currentText() == 'A5/A6' and cb2.currentText() == 'NA':
        view_db1()
    if cb0.currentText() == 'Assembly Area' and cb1.currentText() == 'A13' and cb2.currentText() == 'M00':
        view_db2_M50
        view_db2_M00()
    if cb0.currentText() == 'Assembly Area' and cb1.currentText() == 'A13' and cb2.currentText() == 'M10':
        view_db2_M10()
    if cb0.currentText() == 'Assembly Area' and cb1.currentText() == 'A13' and cb2.currentText() == 'M20':
        view_db2_M20()
    if cb0.currentText() == 'Assembly Area' and cb1.currentText() == 'A13' and cb2.currentText() == 'M30':
        view_db2_M30()
    if cb0.currentText() == 'Assembly Area' and cb1.currentText() == 'A13' and cb2.currentText() == 'M40':
        view_db2_M40()
    if cb0.currentText() == 'Assembly Area' and cb1.currentText() == 'A13' and cb2.currentText() == 'M50':
        view_db2_M50()
    if cb0.currentText() == 'Assembly Area' and cb1.currentText() == 'A13' and cb2.currentText() == 'M60':
        view_db2_M60()
    if cb0.currentText() == 'Assembly Area' and cb1.currentText() == 'A13' and cb2.currentText() == 'M70':
        view_db2_M70()
    if cb0.currentText() == 'Assembly Area' and cb1.currentText() == 'A13' and cb2.currentText() == 'M80':
        view_db2_M80()
    if cb0.currentText() == 'Assembly Area' and cb1.currentText() == 'A13' and cb2.currentText() == 'M90':
        view_db2_M90()
    if cb0.currentText() == 'Assembly Area' and cb1.currentText() == 'A13' and cb2.currentText() == 'M100':
        view_db2_M100()
    if cb0.currentText() == 'Assembly Area' and cb1.currentText() == 'A13' and cb2.currentText() == 'M110':
        view_db2_M110()
    if cb0.currentText() == 'Assembly Area' and cb1.currentText() == 'A13' and cb2.currentText() == 'M120':
        view_db2_M120()
    if cb0.currentText() == 'Assembly Area' and cb1.currentText() == 'Packing' and cb2.currentText() == 'NA':
        view_db3()
    if cb0.currentText() == 'Pre Manufacturing' and cb1.currentText() == 'Plastic Shop' and cb2.currentText() == 'NA':
        view_db_pm1()
    if cb0.currentText() == 'Pre Manufacturing' and cb1.currentText() == 'Metal Shop' and cb2.currentText() == 'NA':
        view_db_pm2()
    if cb0.currentText() == 'Coil Winding' and cb1.currentText() == 'Winding' and cb2.currentText() == 'NA':
        view_db_cw1()
    if cb0.currentText() == 'Coil Winding' and cb1.currentText() == 'Marsili Automation' and cb2.currentText() == 'NA':
        view_db_cw2()
    else:
        alert()


def login_box():
    win = QWidget()
    l1 = QLabel("Enter Username:")
    # un = QLineEdit()
    l2 = QLabel("Enter Password:")
    # psd = QLineEdit()
    fbox = QFormLayout()
    win.setWindowIcon(QIcon('Blue.ico'))
    fbox.addRow(l1, un)
    fbox.addRow(l2, psd)
    button1 = QPushButton("Login")
    fbox.addRow(button1)
    button1.clicked.connect(verify)
    win.setLayout(fbox)
    win.setWindowTitle("Login Credentials")
    win.setStyleSheet("color: #0a3a2a; font-family: Candara; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #ffffff);  padding: 2px; font: 15px; border-width: 2px; ")
    button1.setStyleSheet(
        "color: #0a3a2a; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); border-style:outset; border-width: 2px; border-radius: 10px; border-color: beige;")
    l1.setStyleSheet("border-radius: 3px; border: 1px beige;")
    win.show()
    win.exec_()

def verify():
    if un.text() == 'root' and psd.text() == 'password':
        modify()
    else:
        alert()

def modify():
    win = QWidget()
    b1 = QPushButton("Add New Data Entry")
    b2 = QPushButton("Delete Data Entry")
    b5 = QPushButton("SIRIUS CONTACTOR SO/SOO")
    vbox = QVBoxLayout()
    hbox = QHBoxLayout()
    hbox.addWidget(b1)
    hbox.addStretch()
    hbox.addWidget(b2)
    hbox.addStretch()
    vbox.addWidget(b5)
    vbox.addStretch()
    vbox.addLayout(hbox)
    win.setLayout(vbox)
    win.setWindowIcon(QIcon('Blue.ico'))
    win.setWindowTitle("Troubleshooting")
    win.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #ffffff); padding: 50px; font: 17px; border-width: 2px;")
    b1.setMinimumHeight(100)
    b1.setMinimumWidth(100)
    b2.setMinimumHeight(100)
    b2.setMinimumWidth(100)
    b5.setMaximumHeight(35)
    b5.setFlat(True)
    b1.setFont(QFont('Candara',10))
    b2.setFont(QFont('Candara',10))
    b5.setFont(QFont('Candara',10))
    b5.setStyleSheet("color: #0a3a2a;")
    b1.setStyleSheet(
        "color: #0a3a2a; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); border-style:outset; border-width: 2px; border-radius: 10px; border-color: beige;")
    b2.setStyleSheet(
        "color: #0a3a2a; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); border-style:outset; border-width: 2px; border-radius: 10px; border-color: beige;")

    icon = QIcon("Capture.PNG")
    b5.setIconSize(QSize(100,30))
    b5.setIcon(icon)
    b1.clicked.connect(create_form)
    b2.clicked.connect(delete_form)
    win.show()
    win.exec_()


def delete_form():
    print("")

def create_form():
    wi = QWidget()
    b0 = QPushButton("Select Area:")
    b1 = QPushButton("Select Sub Area:")
    b2 = QPushButton("Select Station ID/Workstation:")
    b3 = QPushButton("")
    b4 = QPushButton("Next")
    b0.setFlat(True)
    b1.setFlat(True)
    b2.setFlat(True)
    b3.setFlat(True)
    b4.setStyleSheet("max-width: 55px;")
    wi.setStyleSheet("background-color:background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #ffffff); padding: 5px; font: 20px; border-width: 2px; Text-align: left;")
    wi.resize(700,100)
    wi.setWindowIcon(QIcon('Blue.ico'))
    wi.setWindowTitle("Enter Data")
    hbox = QHBoxLayout()
    vbox = QVBoxLayout()
    global cb00
    global cb11
    global cb22
    cb00 = QComboBox()
    cb11 = QComboBox()
    cb22 = QComboBox()
    cb00.setStyleSheet("border-radius: 3px; border: 1px beige; font: 15px; padding: 3px; font-family: Candara;")
    cb11.setStyleSheet("border-radius: 3px; border: 1px beige; font: 15px; padding 3px; font-family: Candara;")
    cb22.setStyleSheet("border-radius: 3px; border: 1px beige; font: 15px; padding 3px; font-family: Candara;")
    b4.setStyleSheet(
        "color: #0a3a2a; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); border-style:outset; border-width: 2px; border-radius: 5px; border-color: beige; max-width: 60px; padding: 2px;")
    b0.setFont(QFont('Candara',12))
    b0.setStyleSheet("color: #0a3a2a; Text-align: left; background-color: white")
    b1.setFont(QFont('Candara',12))
    b1.setStyleSheet("color: #0a3a2a; Text-align: left;")
    b2.setFont(QFont('Candara',12))
    b2.setStyleSheet("color: #0a3a2a; Text-align: left;")
    b4.setFont(QFont('Candara',12))
    vbox.addWidget(b0)
    vbox.addStretch()
    vbox.addWidget(cb00)
    vbox.addWidget(b1)
    vbox.addStretch()
    vbox.addWidget(cb11)
    vbox.addWidget(b2)
    vbox.addStretch()
    vbox.addWidget(cb22)
    vbox.addStretch()
    vbox.addWidget(b3)
    vbox.addWidget(b4)

    cb00.addItem("Pre Manufacturing")
    cb00.addItem("Assembly Area")
    cb00.addItem("Coil Winding")


    cb11.addItem("Plastic Shop")
    cb11.addItem("Metal Shop")
    cb11.addItem("A1")
    cb11.addItem("A2")
    cb11.addItem("A3/A4")
    cb11.addItem("A5/A6")
    cb11.addItem("A13")
    cb11.addItem("Packing")
    cb11.addItem("Repair")
    cb11.addItem("Winding")
    cb11.addItem("Winding")
    cb11.addItem("Marsili Automation")

    cb22.addItem("NA")
    cb22.addItem("M00")
    cb22.addItem("M10")
    cb22.addItem("M20")
    cb22.addItem("M30")
    cb22.addItem("M40")
    cb22.addItem("M50")
    cb22.addItem("M60")
    cb22.addItem("M70")
    cb22.addItem("M80")
    cb22.addItem("M90")
    cb22.addItem("M100")
    cb22.addItem("M110")
    cb22.addItem("M120")

    b4.clicked.connect(create_form1)
    vbox.addLayout(hbox)
    wi.setLayout(vbox)
    wi.show()
    wi.exe_()


def create_form1():
    win = QWidget()
    cb = QComboBox()
    win.setWindowIcon(QIcon('Blue.ico'))
    win.setWindowTitle("Enter Data")
    # l0 = QLabel("Serial Number")
    # sn = QLineEdit()
    # l1 = QLabel("Production Area")
    # pa = QLineEdit()
    # l2 = QLabel("Station ID")
    # si = QLineEdit()
    l3 = QLabel("Problem Statement")
    # ps = QLineEdit()
    l4 = QLabel("Preventive Measures")
    # pm = QLineEdit()
    l5 = QLabel("Corrective Measures")
    # cm = QLineEdit()
    fbox = QFormLayout()
    # fbox.addRow(l0,sn)
    # fbox.addRow(l1,pa)
    # fbox.addRow(l2,si)
    fbox.addRow(l3,ps)
    fbox.addRow(l4,pm)
    fbox.addRow(l5,cm)
    button1 = QPushButton("Submit")
    # button2 = QPushButton("Cancel")
    fbox.addRow(button1)
    button1.clicked.connect(update_database)
    win.setLayout(fbox)
    win.resize(700, 100)
    win.setWindowTitle("Add Entry To Database")
    win.setStyleSheet(
        "color: #0a3a2a; font-family: Candara; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #ffffff);  padding: 2px; font: 15px; border-width: 2px; ")
    button1.setStyleSheet(
        "color: #0a3a2a; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); border-style:outset; border-width: 2px; border-radius: 10px; border-color: beige;")
    # l1.setStyleSheet("border-radius: 3px; border: 1px beige;")
    global area
    global subarea
    global  work_station_ID
    area = cb00.currentText()
    subarea = cb11.currentText()
    work_station_ID = cb22.currentText()
    win.show()
    win.exec_()


def update_database():
    connection = pypyodbc.connect('Driver={SQL Server};'
                                  'Server=SIEMENS-PC;'
                                  'Database=Mirror;'
                                  'uid=sa;pwd=1234')
    cursor = connection.cursor()#
    SQLCommand = ("INSERT INTO Mirror2 "
                  "(Area, SubArea, WorkStationID, Problem, PreventiveMeasures, CorrectiveMeasures) "
                  "VALUES (?,?,?,?,?,?)")
    Values = [area, subarea, work_station_ID, ps.text(), pm.text(), cm.text()]
    cursor.execute(SQLCommand,Values)
    connection.commit()
    connection.close()

    w1 = QWidget()
    b1 = QPushButton("Okay")
    b5 = QPushButton("Data successfully updated")
    vbox = QVBoxLayout()
    hbox = QHBoxLayout()
    hbox.addWidget(b1)
    vbox.addWidget(b5)
    vbox.addStretch()
    vbox.addLayout(hbox)
    w1.setLayout(vbox)
    w1.setWindowIcon(QIcon('Blue.ico'))
    w1.setWindowTitle("Troubleshooting")
    w1.setStyleSheet(
        "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #ffffff); padding: 50px; font: 17px; border-width: 2px;")
    b1.setMaximumHeight(35)
    b1.setMinimumWidth(100)
    b5.setMaximumHeight(35)
    b5.setFlat(True)
    b1.setFont(QFont('Candara',10))
    b5.setFont(QFont('Candara',10))
    b5.setStyleSheet("color: #0a3a2a;")
    b1.setStyleSheet(
        "color: #0a3a2a; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); border-style:outset; border-width: 2px; border-radius: 10px; border-color: beige;")

    b1.clicked.connect(lambda: w1.close())
    w1.show()
    w1.exec()



def grid_layout():
    widget = QWidget()
    layout = QGridLayout()
    buttons = {}
    count = 0
    for i in range(3):
        for j in range(5):
            if count > 12:
                break
            else:
                buttons[(i,j)] = QPushButton("M%d0" % count)
                layout.addWidget(buttons[(i,j)],i,j)
            count = count + 1
    buttons[(0,3)].clicked.connect(alert)
    # buttons[(2, 3)].clicked.connect(alert)
    # buttons[(2, 4)].clicked.connect(alert)
    # Linking buttons to corresponding Database Tables
    buttons[(0,0)].clicked.connect(view_db2_M00)
    buttons[(0,1)].clicked.connect(view_db2_M10)
    buttons[(0,2)].clicked.connect(view_db2_M20)
    buttons[(0,4)].clicked.connect(view_db2_M40)
    buttons[(1,0)].clicked.connect(view_db2_M50)
    buttons[(1,1)].clicked.connect(view_db2_M60)
    buttons[(1,2)].clicked.connect(view_db2_M70)
    buttons[(1,3)].clicked.connect(view_db2_M80)
    buttons[(1,4)].clicked.connect(view_db2_M90)
    buttons[(2,0)].clicked.connect(view_db2_M100)
    buttons[(2,1)].clicked.connect(view_db2_M110)
    buttons[(2,2)].clicked.connect(view_db2_M120)
    widget.setLayout(layout)
    widget.setStyleSheet("background-color: white; padding: 50px; font: 17px; border-width: 2px; ")
    widget.setWindowTitle("Select Work Station ID in A13")
    widget.show()
    widget.exec_()


def alert():
    w1 = QWidget()
    b1 = QPushButton("Okay")
    w1.setWindowIcon(QIcon('Blue.ico'))
    b5 = QPushButton("The input is invalid, please try again.")
    vbox = QVBoxLayout()
    hbox = QHBoxLayout()
    hbox.addWidget(b1)
    vbox.addWidget(b5)
    vbox.addStretch()
    vbox.addLayout(hbox)
    w1.setLayout(vbox)
    w1.setWindowTitle("Troubleshooting")
    w1.setStyleSheet(
        "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #ffffff); padding: 50px; font: 17px; border-width: 2px;")
    b1.setMaximumHeight(35)
    b1.setMinimumWidth(100)
    b5.setMaximumHeight(35)
    b5.setFlat(True)
    b1.setFont(QFont('Candara',10))
    b5.setFont(QFont('Candara',10))
    b5.setStyleSheet("color: #0a3a2a;")
    b1.setStyleSheet(
        "color: #0a3a2a; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); border-style:outset; border-width: 2px; border-radius: 10px; border-color: beige;")

    b1.clicked.connect(lambda: w1.close())
    w1.show()
    w1.exec()

# Viewing of Database Tables in A5/A6

def view_db1():
    table = QTableWidget()
    tableItem = QTableWidgetItem()
    connection = pypyodbc.connect('Driver={SQL Server};' 'Server=SIEMENS-PC;' 'Database=Mirror;' 'uid=sa;' 'pwd=1234')
    cursor = connection.cursor()
    sql = (
    "select WorkStationID, Problem, PreventiveMeasures, CorrectiveMeasures from MIRROR2 where SubArea = 'A5/A6'")
    cursor.execute(sql)
    results = cursor.fetchall()
    count_1 = len(results)

    # initiate table
    table.setWindowIcon(QIcon('Blue.ico'))
    table.setWindowTitle("A5/A6(Troubleshooting)")
    table.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
    table.resize(1000,500)
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setRowCount(count_1)
    table.setColumnCount(4)
    stylesheet = "::section{border-color: beige; border-radius: 2px; color: #0a3a2a; Background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #ffffff); font-family: Candara; padding: 20px; font: bold 16px; border-width: 2px; margin: 2px;}"
    table.setStyleSheet("color: #0a3a2a;")
    table.setFont(QFont('Candara',11))
    table.horizontalHeader().setStyleSheet(stylesheet)
    table.verticalHeader().setStyleSheet(stylesheet)
    table.setHorizontalHeaderLabels(
        str("  Station ID  ;    Problem Statement    ;     Preventive Measures     ;  Corrective Measures  ").split(";"))
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setColumnWidth(200,200)
    table.horizontalHeader().setStretchLastSection(True)

    # set data
    for i in range(0, count_1):
        for j in range(0,4):
            table.setItem(i,j,QTableWidgetItem(results[i][j]))
    connection.close()

    # show table
    table.show()
    table.exec_()


# Viewing of Database Tables in Grid Layout

def view_db2_M00():
    table = QTableWidget()
    tableItem = QTableWidgetItem()
    connection = pypyodbc.connect('Driver={SQL Server};' 'Server=SIEMENS-PC;' 'Database=Mirror;' 'uid=sa;' 'pwd=1234')
    cursor = connection.cursor()
    sql = (
        "select WorkStationID, Problem, PreventiveMeasures, CorrectiveMeasures from MIRROR2 where WorkStationID = 'M00'")
    cursor.execute(sql)
    results = cursor.fetchall()
    count_2M00 = len(results)

    # initiate table
    table.setWindowIcon(QIcon('Blue.ico'))
    table.setWindowTitle("A13(Troubleshooting)")
    table.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
    table.resize(1000,500)
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setRowCount(count_2M00)
    table.setColumnCount(4)
    stylesheet = "::section{border-color: beige; border-radius: 2px; color: #0a3a2a; Background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #ffffff); font-family: Candara; padding: 20px; font: bold 16px; border-width: 2px; margin: 2px;}"
    table.setStyleSheet("color: #0a3a2a;")
    table.setFont(QFont('Candara',11))
    table.horizontalHeader().setStyleSheet(stylesheet)
    table.verticalHeader().setStyleSheet(stylesheet)
    table.setHorizontalHeaderLabels(
        str("  Station ID  ;    Problem Statement    ;     Preventive Measures     ;  Corrective Measures  ").split(";"))
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setColumnWidth(200,200)
    table.horizontalHeader().setStretchLastSection(True)

    # set data
    for i in range(0,count_2M00):
        for j in range(0,4):
            table.setItem(i,j,QTableWidgetItem(results[i][j]))

    connection.close()

    # show table
    table.show()
    table.exec_()

def view_db2_M10():
    table = QTableWidget()
    tableItem = QTableWidgetItem()
    connection = pypyodbc.connect('Driver={SQL Server};' 'Server=SIEMENS-PC;' 'Database=Mirror;' 'uid=sa;' 'pwd=1234')
    cursor = connection.cursor()
    sql = (
        "select WorkStationID, Problem, PreventiveMeasures, CorrectiveMeasures from MIRROR2 where WorkStationID = 'M10'")
    cursor.execute(sql)
    results = cursor.fetchall()
    count_2M10 = len(results)

    # initiate table
    table.setWindowIcon(QIcon('Blue.ico'))
    table.setWindowTitle("A13(Troubleshooting)")
    table.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
    table.resize(1000,500)
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setRowCount(count_2M10)
    table.setColumnCount(4)
    stylesheet = "::section{border-color: beige; border-radius: 2px; color: #0a3a2a; Background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #ffffff); font-family: Candara; padding: 20px; font: bold 16px; border-width: 2px; margin: 2px;}"
    table.setStyleSheet("color: #0a3a2a;")
    table.setFont(QFont('Candara',11))
    table.horizontalHeader().setStyleSheet(stylesheet)
    table.verticalHeader().setStyleSheet(stylesheet)
    table.setHorizontalHeaderLabels(
        str("  Station ID  ;    Problem Statement    ;     Preventive Measures     ;  Corrective Measures  ").split(";"))
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setColumnWidth(200,200)
    table.horizontalHeader().setStretchLastSection(True)
    # set data
    for i in range(0,count_2M10):
        for j in range(0,4):
            table.setItem(i,j,QTableWidgetItem(results[i][j]))

    connection.close()

    # show table
    table.show()
    table.exec_()


def view_db2_M20():
    table = QTableWidget()
    tableItem = QTableWidgetItem()
    connection = pypyodbc.connect('Driver={SQL Server};' 'Server=SIEMENS-PC;' 'Database=Mirror;' 'uid=sa;' 'pwd=1234')
    cursor = connection.cursor()
    sql = (
        "select WorkStationID, Problem, PreventiveMeasures, CorrectiveMeasures from MIRROR2 where WorkStationID = 'M20'")
    cursor.execute(sql)
    results = cursor.fetchall()
    count_2M20 = len(results)

    # initiate table
    table.setWindowIcon(QIcon('Blue.ico'))
    table.setWindowTitle("A13(Troubleshooting)")
    table.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
    table.resize(1000,500)
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setRowCount(count_2M20)
    table.setColumnCount(4)
    stylesheet = "::section{border-color: beige; border-radius: 2px; color: #0a3a2a; Background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #ffffff); font-family: Candara; padding: 20px; font: bold 16px; border-width: 2px; margin: 2px;}"
    table.setStyleSheet("color: #0a3a2a;")
    table.setFont(QFont('Candara',11))
    table.horizontalHeader().setStyleSheet(stylesheet)
    table.verticalHeader().setStyleSheet(stylesheet)
    table.setHorizontalHeaderLabels(
        str("  Station ID  ;    Problem Statement    ;     Preventive Measures     ;  Corrective Measures  ").split(";"))
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setColumnWidth(200,200)
    table.horizontalHeader().setStretchLastSection(True)

    # set data
    for i in range(0,count_2M20):
        for j in range(0,4):
            table.setItem(i,j,QTableWidgetItem(results[i][j]))

    connection.close()

    # show table
    table.show()
    table.exec_()


def view_db2_M30():
    table = QTableWidget()
    tableItem = QTableWidgetItem()
    connection = pypyodbc.connect('Driver={SQL Server};' 'Server=SIEMENS-PC;' 'Database=Mirror;' 'uid=sa;' 'pwd=1234')
    cursor = connection.cursor()
    sql = (
        "select WorkStationID, Problem, PreventiveMeasures, CorrectiveMeasures from MIRROR2 where WorkStationID = 'M30'")
    cursor.execute(sql)
    results = cursor.fetchall()
    count_2M30 = len(results)

    # initiate table
    table.setWindowIcon(QIcon('Blue.ico'))
    table.setWindowTitle("A13(Troubleshooting)")
    table.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
    table.resize(1000,500)
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setRowCount(count_2M30)
    table.setColumnCount(4)
    stylesheet = "::section{border-color: beige; border-radius: 2px; color: #0a3a2a; Background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #ffffff); font-family: Candara; padding: 20px; font: bold 16px; border-width: 2px; margin: 2px;}"
    table.setStyleSheet("color: #0a3a2a;")
    table.setFont(QFont('Candara',11))
    table.horizontalHeader().setStyleSheet(stylesheet)
    table.verticalHeader().setStyleSheet(stylesheet)
    table.setHorizontalHeaderLabels(
        str("  Station ID  ;    Problem Statement    ;     Preventive Measures     ;  Corrective Measures  ").split(";"))
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setColumnWidth(200,200)
    table.horizontalHeader().setStretchLastSection(True)

    # set data
    for i in range(0,count_2M30):
        for j in range(0,4):
            table.setItem(i,j,QTableWidgetItem(results[i][j]))

    connection.close()

    # show table
    table.show()
    table.exec_()


def view_db2_M40():
    table = QTableWidget()
    tableItem = QTableWidgetItem()
    connection = pypyodbc.connect('Driver={SQL Server};' 'Server=SIEMENS-PC;' 'Database=Mirror;' 'uid=sa;' 'pwd=1234')
    cursor = connection.cursor()
    sql = (
        "select WorkStationID, Problem, PreventiveMeasures, CorrectiveMeasures from MIRROR2 where WorkStationID = 'M40'")
    cursor.execute(sql)
    results = cursor.fetchall()
    count_2M40 = len(results)

    # initiate table
    table.setWindowIcon(QIcon('Blue.ico'))
    table.setWindowTitle("A13(Troubleshooting)")
    table.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
    table.resize(1000,500)
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setRowCount(count_2M40)
    table.setColumnCount(4)
    stylesheet = "::section{border-color: beige; border-radius: 2px; color: #0a3a2a; Background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #ffffff); font-family: Candara; padding: 20px; font: bold 16px; border-width: 2px; margin: 2px;}"
    table.setStyleSheet("color: #0a3a2a;")
    table.setFont(QFont('Candara',11))
    table.horizontalHeader().setStyleSheet(stylesheet)
    table.verticalHeader().setStyleSheet(stylesheet)
    table.setHorizontalHeaderLabels(
        str("  Station ID  ;    Problem Statement    ;     Preventive Measures     ;  Corrective Measures  ").split(";"))
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setColumnWidth(200,200)
    table.horizontalHeader().setStretchLastSection(True)
    # set data
    for i in range(0,count_2M40):
        for j in range(0,4):
            table.setItem(i,j,QTableWidgetItem(results[i][j]))

    connection.close()

    # show table
    table.show()
    table.exec_()

def view_db2_M50():
    table = QTableWidget()
    tableItem = QTableWidgetItem()
    connection = pypyodbc.connect('Driver={SQL Server};' 'Server=SIEMENS-PC;' 'Database=Mirror;' 'uid=sa;' 'pwd=1234')
    cursor = connection.cursor()
    sql = (
        "select WorkStationID, Problem, PreventiveMeasures, CorrectiveMeasures from MIRROR2 where WorkStationID = 'M50/M50B'")
    cursor.execute(sql)
    results = cursor.fetchall()
    count_2M50 = len(results)

    # initiate table
    table.setWindowIcon(QIcon('Blue.ico'))
    table.setWindowTitle("A13(Troubleshooting)")
    table.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
    table.resize(1000,500)
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setRowCount(count_2M50)
    table.setColumnCount(4)
    stylesheet = "::section{border-color: beige; border-radius: 2px; color: #0a3a2a; Background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #ffffff); font-family: Candara; padding: 20px; font: bold 16px; border-width: 2px; margin: 2px;}"
    table.setStyleSheet("color: #0a3a2a;")
    table.setFont(QFont('Candara',11))
    table.horizontalHeader().setStyleSheet(stylesheet)
    table.verticalHeader().setStyleSheet(stylesheet)
    table.setHorizontalHeaderLabels(
        str("  Station ID  ;    Problem Statement    ;     Preventive Measures     ;  Corrective Measures  ").split(";"))
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setColumnWidth(200,200)
    table.horizontalHeader().setStretchLastSection(True)

    # set data
    for i in range(0,count_2M50):
        for j in range(0,4):
            table.setItem(i,j,QTableWidgetItem(results[i][j]))

    connection.close()

    # show table
    table.show()
    table.exec_()


def view_db2_M60():
    table = QTableWidget()
    tableItem = QTableWidgetItem()
    connection = pypyodbc.connect('Driver={SQL Server};' 'Server=SIEMENS-PC;' 'Database=Mirror;' 'uid=sa;' 'pwd=1234')
    cursor = connection.cursor()
    sql = (
        "select WorkStationID, Problem, PreventiveMeasures, CorrectiveMeasures from MIRROR2 where WorkStationID = 'M60A' or StationID = 'M60B'")
    cursor.execute(sql)
    results = cursor.fetchall()
    count_2M60 = len(results)

    # initiate table
    table.setWindowIcon(QIcon('Blue.ico'))
    table.setWindowTitle("A13(Troubleshooting)")
    table.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
    table.resize(1000,500)
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setRowCount(count_2M60)
    table.setColumnCount(4)
    stylesheet = "::section{border-color: beige; border-radius: 2px; color: #0a3a2a; Background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #ffffff); font-family: Candara; padding: 20px; font: bold 16px; border-width: 2px; margin: 2px;}"
    table.setStyleSheet("color: #0a3a2a;")
    table.setFont(QFont('Candara',11))
    table.horizontalHeader().setStyleSheet(stylesheet)
    table.verticalHeader().setStyleSheet(stylesheet)
    table.setHorizontalHeaderLabels(
        str("  Station ID  ;    Problem Statement    ;     Preventive Measures     ;  Corrective Measures  ").split(";"))
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setColumnWidth(200,200)
    table.horizontalHeader().setStretchLastSection(True)

    # set data
    for i in range(0,count_2M60):
        for j in range(0,4):
            table.setItem(i,j,QTableWidgetItem(results[i][j]))

    connection.close()

    # show table
    table.show()
    table.exec_()

def view_db2_M70():
    table = QTableWidget()
    tableItem = QTableWidgetItem()
    connection = pypyodbc.connect('Driver={SQL Server};' 'Server=SIEMENS-PC;' 'Database=Mirror;' 'uid=sa;' 'pwd=1234')
    cursor = connection.cursor()
    sql = (
        "select WorkStationID, Problem, PreventiveMeasures, CorrectiveMeasures from MIRROR2 where WorkStationID = 'M70'")
    cursor.execute(sql)
    results = cursor.fetchall()
    count_2M70 = len(results)

    # initiate table
    table.setWindowIcon(QIcon('Blue.ico'))
    table.setWindowTitle("A13(Troubleshooting)")
    table.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
    table.resize(1000,500)
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setRowCount(count_2M70)
    table.setColumnCount(4)
    stylesheet = "::section{border-color: beige; border-radius: 2px; color: #0a3a2a; Background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #ffffff); font-family: Candara; padding: 20px; font: bold 16px; border-width: 2px; margin: 2px;}"
    table.setStyleSheet("color: #0a3a2a;")
    table.setFont(QFont('Candara',11))
    table.horizontalHeader().setStyleSheet(stylesheet)
    table.verticalHeader().setStyleSheet(stylesheet)
    table.setHorizontalHeaderLabels(
        str("  Station ID  ;    Problem Statement    ;     Preventive Measures     ;  Corrective Measures  ").split(";"))
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setColumnWidth(200,200)
    table.horizontalHeader().setStretchLastSection(True)

    # set data
    for i in range(0,count_2M70):
        for j in range(0,4):
            table.setItem(i,j,QTableWidgetItem(results[i][j]))

    connection.close()

    # show table
    table.show()
    table.exec_()


def view_db2_M80():
    table = QTableWidget()
    tableItem = QTableWidgetItem()
    connection = pypyodbc.connect('Driver={SQL Server};' 'Server=SIEMENS-PC;' 'Database=Mirror;' 'uid=sa;' 'pwd=1234')
    cursor = connection.cursor()
    sql = (
        "select WorkStationID, Problem, PreventiveMeasures, CorrectiveMeasures from MIRROR2 where WorkStationID = 'M80A/M80B'")
    cursor.execute(sql)
    results = cursor.fetchall()
    count_2M80 = len(results)

    # initiate table
    table.setWindowIcon(QIcon('Blue.ico'))
    table.setWindowTitle("A13(Troubleshooting)")
    table.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
    table.resize(1000,500)
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setRowCount(count_2M80)
    table.setColumnCount(4)
    stylesheet = "::section{border-color: beige; border-radius: 2px; color: #0a3a2a; Background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #ffffff); font-family: Candara; padding: 20px; font: bold 16px; border-width: 2px; margin: 2px;}"
    table.setStyleSheet("color: #0a3a2a;")
    table.setFont(QFont('Candara',11))
    table.horizontalHeader().setStyleSheet(stylesheet)
    table.verticalHeader().setStyleSheet(stylesheet)
    table.setHorizontalHeaderLabels(
        str("  Station ID  ;    Problem Statement    ;     Preventive Measures     ;  Corrective Measures  ").split(";"))
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setColumnWidth(200,200)
    table.horizontalHeader().setStretchLastSection(True)

    # set data
    for i in range(0,count_2M80):
        for j in range(0,4):
            table.setItem(i,j,QTableWidgetItem(results[i][j]))

    connection.close()

    # show table
    table.show()
    table.exec_()


def view_db2_M90():
    table = QTableWidget()
    tableItem = QTableWidgetItem()
    connection = pypyodbc.connect('Driver={SQL Server};' 'Server=SIEMENS-PC;' 'Database=Mirror;' 'uid=sa;' 'pwd=1234')
    cursor = connection.cursor()
    sql = (
        "select WorkStationID, Problem, PreventiveMeasures, CorrectiveMeasures from MIRROR2 where WorkStationID = 'M90A/M90B'")
    cursor.execute(sql)
    results = cursor.fetchall()
    count_2M90 = len(results)

    # initiate table
    table.setWindowIcon(QIcon('Blue.ico'))
    table.setWindowTitle("A13(Troubleshooting)")
    table.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
    table.resize(1000,500)
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setRowCount(count_2M90)
    table.setColumnCount(4)
    stylesheet = "::section{border-color: beige; border-radius: 2px; color: #0a3a2a; Background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #ffffff); font-family: Candara; padding: 20px; font: bold 16px; border-width: 2px; margin: 2px;}"
    table.setStyleSheet("color: #0a3a2a;")
    table.setFont(QFont('Candara',11))
    table.horizontalHeader().setStyleSheet(stylesheet)
    table.verticalHeader().setStyleSheet(stylesheet)
    table.setHorizontalHeaderLabels(
        str("  Station ID  ;    Problem Statement    ;     Preventive Measures     ;  Corrective Measures  ").split(";"))
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setColumnWidth(200,200)
    table.horizontalHeader().setStretchLastSection(True)

    # set data
    for i in range(0,count_2M90):
        for j in range(0,4):
            table.setItem(i,j,QTableWidgetItem(results[i][j]))

    connection.close()

    # show table
    table.show()
    table.exec_()


def view_db2_M100():
    table = QTableWidget()
    tableItem = QTableWidgetItem()
    connection = pypyodbc.connect('Driver={SQL Server};' 'Server=SIEMENS-PC;' 'Database=Mirror;' 'uid=sa;' 'pwd=1234')
    cursor = connection.cursor()
    sql = (
        "select WorkStationID, Problem, PreventiveMeasures, CorrectiveMeasures from MIRROR2 where WorkStationID = 'M100'")
    cursor.execute(sql)
    results = cursor.fetchall()
    count_2M100 = len(results)

    # initiate table
    table.setWindowIcon(QIcon('Blue.ico'))
    table.setWindowTitle("A13(Troubleshooting)")
    table.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
    table.resize(1000,500)
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setRowCount(count_2M100)
    table.setColumnCount(4)
    stylesheet = "::section{border-color: beige; border-radius: 2px; color: #0a3a2a; Background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #ffffff); font-family: Candara; padding: 20px; font: bold 16px; border-width: 2px; margin: 2px;}"
    table.setStyleSheet("color: #0a3a2a;")
    table.setFont(QFont('Candara',11))
    table.horizontalHeader().setStyleSheet(stylesheet)
    table.verticalHeader().setStyleSheet(stylesheet)
    table.setHorizontalHeaderLabels(
        str("  Station ID  ;    Problem Statement    ;     Preventive Measures     ;  Corrective Measures  ").split(";"))
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setColumnWidth(200,200)
    table.horizontalHeader().setStretchLastSection(True)

    # set data
    for i in range(0,count_2M100):
        for j in range(0,4):
            table.setItem(i,j,QTableWidgetItem(results[i][j]))

    connection.close()

    # show table
    table.show()
    table.exec_()


def view_db2_M110():
    table = QTableWidget()
    tableItem = QTableWidgetItem()
    connection = pypyodbc.connect('Driver={SQL Server};' 'Server=SIEMENS-PC;' 'Database=Mirror;' 'uid=sa;' 'pwd=1234')
    cursor = connection.cursor()
    sql = (
        "select WorkStationID, Problem, PreventiveMeasures, CorrectiveMeasures from MIRROR2 where WorkStationID = 'M110/M120'")
    cursor.execute(sql)
    results = cursor.fetchall()
    count_2M110 = len(results)

    # initiate table
    table.setWindowIcon(QIcon('Blue.ico'))
    table.setWindowTitle("A13(Troubleshooting)")
    table.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
    table.resize(1000,500)
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setRowCount(count_2M110)
    table.setColumnCount(4)
    stylesheet = "::section{border-color: beige; border-radius: 2px; color: #0a3a2a; Background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #ffffff); font-family: Candara; padding: 20px; font: bold 16px; border-width: 2px; margin: 2px;}"
    table.setStyleSheet("color: #0a3a2a;")
    table.setFont(QFont('Candara',11))
    table.horizontalHeader().setStyleSheet(stylesheet)
    table.verticalHeader().setStyleSheet(stylesheet)
    table.setHorizontalHeaderLabels(
        str("  Station ID  ;    Problem Statement    ;     Preventive Measures     ;  Corrective Measures  ").split(";"))
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setColumnWidth(200,200)
    table.horizontalHeader().setStretchLastSection(True)

    # set data
    for i in range(0,count_2M110):
        for j in range(0,4):
            table.setItem(i,j,QTableWidgetItem(results[i][j]))

    connection.close()

    # show table
    table.show()
    table.exec_()


def view_db2_M120():
    table = QTableWidget()
    tableItem = QTableWidgetItem()
    connection = pypyodbc.connect('Driver={SQL Server};' 'Server=SIEMENS-PC;' 'Database=Mirror;' 'uid=sa;' 'pwd=1234')
    cursor = connection.cursor()
    sql = (
        "select WorkStationID, Problem, PreventiveMeasures, CorrectiveMeasures from MIRROR2 where WorkStationID = 'M110/M120'")
    cursor.execute(sql)
    results = cursor.fetchall()
    count_2M120 = len(results)

    # initiate table
    table.setWindowIcon(QIcon('Blue.ico'))
    table.setWindowTitle("A13(Troubleshooting)")
    table.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
    table.resize(1000,500)
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setRowCount(count_2M120)
    table.setColumnCount(4)
    stylesheet = "::section{border-color: beige; border-radius: 2px; color: #0a3a2a; Background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #ffffff); font-family: Candara; padding: 20px; font: bold 16px; border-width: 2px; margin: 2px;}"
    table.setStyleSheet("color: #0a3a2a;")
    table.setFont(QFont('Candara',11))
    table.horizontalHeader().setStyleSheet(stylesheet)
    table.verticalHeader().setStyleSheet(stylesheet)
    table.setHorizontalHeaderLabels(
        str("  Station ID  ;    Problem Statement    ;     Preventive Measures     ;  Corrective Measures  ").split(";"))
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setColumnWidth(200,200)
    table.horizontalHeader().setStretchLastSection(True)

    # set data
    for i in range(0,count_2M120):
        for j in range(0,4):
            table.setItem(i,j,QTableWidgetItem(results[i][j]))

    connection.close()

    # show table
    table.show()
    table.exec_()


# Viewing of Database Tables in Packing

def view_db3():
    table = QTableWidget()
    tableItem = QTableWidgetItem()
    connection = pypyodbc.connect('Driver={SQL Server};' 'Server=SIEMENS-PC;' 'Database=Mirror;' 'uid=sa;' 'pwd=1234')
    cursor = connection.cursor()
    sql = (
        "select WorkStationID, Problem, PreventiveMeasures, CorrectiveMeasures from MIRROR2 where SubArea = 'Packing'")
    cursor.execute(sql)
    results = cursor.fetchall()
    count_3 = len(results)

    # initiate table
    table.setWindowIcon(QIcon('Blue.ico'))
    table.setWindowTitle("Packing(Troubleshooting)")
    table.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
    table.resize(1000,500)
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setRowCount(count_3)
    table.setColumnCount(4)
    stylesheet = "::section{border-color: beige; border-radius: 2px; color: #0a3a2a; Background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #ffffff); font-family: Candara; padding: 20px; font: bold 16px; border-width: 2px; margin: 2px;}"
    table.setStyleSheet("color: #0a3a2a;")
    table.setFont(QFont('Candara',11))
    table.horizontalHeader().setStyleSheet(stylesheet)
    table.verticalHeader().setStyleSheet(stylesheet)
    table.setHorizontalHeaderLabels(
        str("  Station ID  ;    Problem Statement    ;     Preventive Measures     ;  Corrective Measures  ").split(";"))
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setColumnWidth(200,200)
    table.horizontalHeader().setStretchLastSection(True)

    # set data
    for i in range(0,count_3):
        for j in range(0,4):
            table.setItem(i,j,QTableWidgetItem(results[i][j]))

    connection.close()

    # show table
    table.show()
    table.exec_()


def view_db_pm1():
    table = QTableWidget()
    tableItem = QTableWidgetItem()
    connection = pypyodbc.connect('Driver={SQL Server};' 'Server=SIEMENS-PC;' 'Database=Mirror;' 'uid=sa;' 'pwd=1234')
    cursor = connection.cursor()
    sql = (
        "select SubArea, WorkStationID, Problem, PreventiveMeasures, CorrectiveMeasures from MIRROR2 where SubArea = 'Plastic Shop'")
    cursor.execute(sql)
    results = cursor.fetchall()
    count_pm1 = len(results)

    # initiate table
    table.setWindowIcon(QIcon('Blue.ico'))
    table.setWindowTitle("Packing(Troubleshooting)")
    table.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
    table.resize(1000,500)
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setRowCount(count_pm1)
    table.setColumnCount(5)
    stylesheet = "::section{border-color: beige; border-radius: 2px; color: #0a3a2a; Background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #ffffff); font-family: Candara; padding: 20px; font: bold 16px; border-width: 2px; margin: 2px;}"
    table.setStyleSheet("color: #0a3a2a;")
    table.setFont(QFont('Candara',11))
    table.horizontalHeader().setStyleSheet(stylesheet)
    table.verticalHeader().setStyleSheet(stylesheet)
    table.setHorizontalHeaderLabels(
        str("   Sub Area   ;  Station ID  ;    Problem Statement    ;     Preventive Measures     ;  Corrective Measures  ").split(
            ";"))
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setColumnWidth(200,200)
    table.horizontalHeader().setStretchLastSection(True)

    # set data
    for i in range(0,count_pm1):
        for j in range(0,5):
            table.setItem(i,j,QTableWidgetItem(results[i][j]))

    connection.close()

    # show table
    table.show()
    table.exec_()

def view_db_pm2():
    table = QTableWidget()
    tableItem = QTableWidgetItem()
    connection = pypyodbc.connect('Driver={SQL Server};' 'Server=SIEMENS-PC;' 'Database=Mirror;' 'uid=sa;' 'pwd=1234')
    cursor = connection.cursor()
    sql = (
        "select SubArea, WorkStationID, Problem, PreventiveMeasures, CorrectiveMeasures from MIRROR2 where SubArea = 'Metal Shop'")
    cursor.execute(sql)
    results = cursor.fetchall()
    count_pm2 = len(results)

    # initiate table
    table.setWindowIcon(QIcon('Blue.ico'))
    table.setWindowTitle("Packing(Troubleshooting)")
    table.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
    table.resize(1000,500)
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setRowCount(count_pm2)
    table.setColumnCount(5)
    stylesheet = "::section{border-color: beige; border-radius: 2px; color: #0a3a2a; Background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #ffffff); font-family: Candara; padding: 20px; font: bold 16px; border-width: 2px; margin: 2px;}"
    table.setStyleSheet("color: #0a3a2a;")
    table.setFont(QFont('Candara',11))
    table.horizontalHeader().setStyleSheet(stylesheet)
    table.verticalHeader().setStyleSheet(stylesheet)
    table.setHorizontalHeaderLabels(
        str("   Sub Area   ;  Station ID  ;    Problem Statement    ;     Preventive Measures     ;  Corrective Measures  ").split(
            ";"))
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setColumnWidth(200,200)
    table.horizontalHeader().setStretchLastSection(True)

    # set data
    for i in range(0,count_pm2):
        for j in range(0,5):
            table.setItem(i,j,QTableWidgetItem(results[i][j]))

    connection.close()

    # show table
    table.show()
    table.exec_()


def view_db_cw1():
    table = QTableWidget()
    tableItem = QTableWidgetItem()
    connection = pypyodbc.connect('Driver={SQL Server};' 'Server=SIEMENS-PC;' 'Database=Mirror;' 'uid=sa;' 'pwd=1234')
    cursor = connection.cursor()
    sql = (
        "select SubArea, WorkStationID, Problem, PreventiveMeasures, CorrectiveMeasures from MIRROR2 where SubArea = 'Winding'")
    cursor.execute(sql)
    results = cursor.fetchall()
    count_cw1 = len(results)

    # initiate table
    table.setWindowIcon(QIcon('Blue.ico'))
    table.setWindowTitle("Packing(Troubleshooting)")
    table.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
    table.resize(1000,500)
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setRowCount(count_cw1)
    table.setColumnCount(5)
    stylesheet = "::section{border-color: beige; border-radius: 2px; color: #0a3a2a; Background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #ffffff); font-family: Candara; padding: 20px; font: bold 16px; border-width: 2px; margin: 2px;}"
    table.setStyleSheet("color: #0a3a2a;")
    table.setFont(QFont('Candara',11))
    table.horizontalHeader().setStyleSheet(stylesheet)
    table.verticalHeader().setStyleSheet(stylesheet)
    table.setHorizontalHeaderLabels(
        str("   Sub Area   ;  Station ID  ;    Problem Statement    ;     Preventive Measures     ;  Corrective Measures  ").split(
            ";"))
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setColumnWidth(200,200)
    table.horizontalHeader().setStretchLastSection(True)

    # set data
    for i in range(0,count_cw1):
        for j in range(0,5):
            table.setItem(i,j,QTableWidgetItem(results[i][j]))

    connection.close()

    # show table
    table.show()
    table.exec_()

def view_db_cw2():
    table = QTableWidget()
    tableItem = QTableWidgetItem()
    connection = pypyodbc.connect('Driver={SQL Server};' 'Server=SIEMENS-PC;' 'Database=Mirror;' 'uid=sa;' 'pwd=1234')
    cursor = connection.cursor()
    sql = (
        "select SubArea, WorkStationID, Problem, PreventiveMeasures, CorrectiveMeasures from MIRROR2 where SubArea = 'Plastic Shop'")
    cursor.execute(sql)
    results = cursor.fetchall()
    count_cw2 = len(results)

    # initiate table
    table.setWindowIcon(QIcon('Blue.ico'))
    table.setWindowTitle("Packing(Troubleshooting)")
    table.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
    table.resize(1000,500)
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setRowCount(count_cw2)
    table.setColumnCount(5)
    stylesheet = "::section{border-color: beige; border-radius: 2px; color: #0a3a2a; Background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #ffffff); font-family: Candara; padding: 20px; font: bold 16px; border-width: 2px; margin: 2px;}"
    table.setStyleSheet("color: #0a3a2a;")
    table.setFont(QFont('Candara',11))
    table.horizontalHeader().setStyleSheet(stylesheet)
    table.verticalHeader().setStyleSheet(stylesheet)
    table.setHorizontalHeaderLabels(
        str("   Sub Area   ;  Station ID  ;    Problem Statement    ;     Preventive Measures     ;  Corrective Measures  ").split(
            ";"))
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    table.setColumnWidth(200,200)
    table.horizontalHeader().setStretchLastSection(True)

    # set data
    for i in range(0,count_cw2):
        for j in range(0,5):
            table.setItem(i,j,QTableWidgetItem(results[i][j]))

    connection.close()

    # show table
    table.show()
    table.exec_()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    # sn = QLineEdit()
    pa = QLineEdit()
    si = QLineEdit()
    ps = QLineEdit()
    pm = QLineEdit()
    cm = QLineEdit()

    un = QLineEdit()
    psd = QLineEdit()

    window()
    sys.exit(app.exec_())
