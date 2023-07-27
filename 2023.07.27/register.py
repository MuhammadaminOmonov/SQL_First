import mysql.connector
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from os import system as sys
sys("cls")

class Databaza:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="32!V996g" # o'zingizning parolingiz
        )
        self.cursor = self.mydb.cursor()

        self.dbConnection()
        self.createTable()

    def dbConnection(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS users_data;")
        self.cursor.execute("USE users_data;")


    def createTable(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                full_name varchar(100) NOT NULL,
                username varchar(50) NOT NULL,
                password varchar(32) NOT NULL
            );
        """)



    def insertData(self, full_name, username, password):
        self.cursor.execute(f"""
            INSERT INTO users (full_name, username, password) VALUES ('{full_name}', '{username}', '{password}');
        """)
        self.mydb.commit()
    
    def selectData(self):
        self.cursor.execute("SELECT * FROM users;")
        malumot = self.cursor.fetchall()
        return malumot
    
    def selectDataFromFullName(self, full_name):
        self.cursor.execute(f"SELECT * FROM users WHERE full_name = '{full_name}';")
        malumot = self.cursor.fetchall()
        return malumot

    def deleteData(self, id: int):
        self.cursor.execute(f"""
            DELETE FROM users WHERE id = {id};
        """)
        self.mydb.commit()

class Label(QLabel):
    def __init__(self, text: str, oyna: QWidget):
        super().__init__(text, oyna)
        self.setStyleSheet("""
            color: #FF0000;
            font-size: 25px;
            background-color: #2245BD;
            font-weight: bold;
            padding: 0.5em;
        """)

class LineEdit(QLineEdit):
    def __init__(self, oyna: QWidget):
        super().__init__(oyna)
        self.setStyleSheet("""
            color: #0000FF;
            font-size: 25px;
            font-family: monospace;
            background-color: #FFFFFF;
            padding: 0.7em
        """)
        
class Button(QPushButton):
    def __init__(self, text: str, oyna: QWidget):
        super().__init__(text, oyna)
        self.setStyleSheet("""
            background-color: yellow;
            padding: 15px;
        """)



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.move(600, 150)
        self.setFixedSize(600, 680)
        self.setWindowTitle("Register page")
        self.setWindowIcon(QIcon("C:\\Users\\HP\\Desktop\\calculator\\calculator.png"))

        self.main_box = QVBoxLayout(self)

        self.button_box_start = QHBoxLayout(self)
        self.sign_up = Button("Sign Up", self)
        self.sign_up.clicked.connect(lambda: sign_up_page(self))
        self.sign_in = Button("Sign In", self)
        self.sign_up.clicked.connect(lambda: sign_in_page(self))
        self.button_box_start.addWidget(self.sign_up)
        self.button_box_start.addWidget(self.sign_in)
        def sign_up_page(self):
            pass

        def sign_in_page(self):
            pass
        
        self.fullName_label = Label("Fullname", self)
        self.fullName_Input = LineEdit(self)

        self.userName_label = Label("Username", self)
        self.userName_Input = LineEdit(self)
        
        self.password_label = Label("Password", self)
        self.password_Input = LineEdit(self)
        self.password_Input.setPlaceholderText("Kamida 8 belgidan iborat bo'lishi kerak")


        self.button_box = QHBoxLayout(self)
        self.button_clear = Button("CLEAR", self)
        self.button_clear.clicked.connect(lambda: func_clear(self.fullName_Input, self.userName_Input, self.password_Input))
        self.button_submit = Button("SUBMIT", self)
        self.button_submit.clicked.connect(lambda: func_submit(self))
        def func_clear(fullName_Input, userName_Input, password_Input):
            fullName_Input.clear()
            userName_Input.clear()
            password_Input.clear()

        def func_submit(self):
            if len(self.userName_Input.text()) > 0 and len(self.password_Input.text()) > 8:
                self.notice_blank = QMessageBox(self)
                self.notice_blank.setWindowTitle("Eslatma")
                self.notice_blank.setText("Ro'yxatdan o'tdingiz")
                self.notice_blank.setStyleSheet("background-color: white;")
                self.notice_blank.exec_()
            else:
                self.notice_blank = QMessageBox(self)
                self.notice_blank.setWindowTitle("Eslatma")
                self.notice_blank.setText("Ro'yxatdan o'tmadingiz")
                self.notice_blank.setStyleSheet("background-color: white;")
                self.notice_blank.exec_()

        self.button_box.addWidget(self.button_clear)
        self.button_box.addWidget(self.button_submit)

        self.main_box.addLayout(self.button_box_start)
        self.main_box.addWidget(self.fullName_label)
        self.main_box.addWidget(self.fullName_Input)
        self.main_box.addWidget(self.userName_label)
        self.main_box.addWidget(self.userName_Input)
        self.main_box.addWidget(self.password_label)
        self.main_box.addWidget(self.password_Input)
        self.main_box.addLayout(self.button_box)

app = QApplication([])
window = Window()
window.show()
app.exec_()