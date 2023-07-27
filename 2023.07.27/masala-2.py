import mysql.connector
import datetime
from os import system

class Databaza:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="unkown" # o'zingizning parolingiz
        )
        self.cursor = self.mydb.cursor()

        self.dbConnection()
        self.createTable()
        self.insertData()

    def dbConnection(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS users_data;")
        self.cursor.execute("USE users_data;")


    def createTable(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER,
                name VARCHAR(255) NOT NULL,
                surname VARCHAR(255) NOT NULL,
                password INTEGER NOT NULL,
                age INTEGER NOT NULL,
                username VARCHAR(100) NOT NULL,
                gender VARCHAR(100) NOT NULL
            );
        """)


    def insertData(self):
        self.cursor.execute("""
            insert into users (id, name, surname, password, age, username, gender) values (1, 'Thaddeus', 'Read', 598233, 27.6, 'tread0', 'Male'),
                (2, 'Ingelbert', 'Duckinfield', 938213, 33.9, 'iduckinfield1', 'Male'),
                (3, 'Fionnula', 'Spire', 928619, 70.7, 'fspire2', 'Female'),
                (4, 'Maurine', 'Follitt', 1050819, 43.5, 'mfollitt3', 'Female'),
                (5, 'Cob', 'Northall', 587228, 32.6, 'cnorthall4', 'Male'),
                (6, 'Bailie', 'Vivians', 804596, 69.3, 'bvivians5', 'Male'),
                (7, 'Lennard', 'Maharey', 535853, 1.0, 'lmaharey6', 'Male'),
                (8, 'Melicent', 'Segebrecht', 801653, 23.7, 'msegebrecht7', 'Female'),
                (9, 'Gabe', 'Jerrold', 960583, 35.4, 'gjerrold8', 'Male'),
                (10, 'Katina', 'Tebbs', 674519, 46.1, 'ktebbs9', 'Female'),
                (11, 'Rafe', 'Heistermann', 154776, 41.7, 'rheistermanna', 'Polygender'),
                (12, 'Birdie', 'Truelove', 1078137, 3.0, 'btrueloveb', 'Genderqueer'),
                (13, 'Archibold', 'Forbes', 140050, 6.5, 'aforbesc', 'Male'),
                (14, 'Tanner', 'Hamerton', 880680, 91.2, 'thamertond', 'Male'),
                (15, 'Amalle', 'Riddich', 248183, 97.0, 'ariddiche', 'Female'),
                (16, 'Zonda', 'Green', 374148, 27.3, 'zgreenf', 'Female'),
                (17, 'Forster', 'Lancett', 819079, 46.3, 'flancettg', 'Non-binary'),
                (18, 'Renelle', 'Speerman', 457158, 72.0, 'rspeermanh', 'Female'),
                (19, 'Aldon', 'Pervoe', 456336, 46.7, 'apervoei', 'Male'),
                (20, 'Willem', 'Aidler', 865413, 90.3, 'waidlerj', 'Male'),
                (21, 'Dorie', 'Mongain', 672294, 81.6, 'dmongaink', 'Male'),
                (22, 'Mufinella', 'Kyncl', 921351, 49.5, 'mkyncll', 'Female'),
                (23, 'Arleyne', 'Daville', 769493, 47.9, 'adavillem', 'Female'),
                (24, 'Dwight', 'Rives', 658503, 56.6, 'drivesn', 'Male'),
                (25, 'Nata', 'Vasilyev', 625178, 38.0, 'nvasilyevo', 'Non-binary'),
                (26, 'Alexandrina', 'Cottrell', 180514, 7.7, 'acottrellp', 'Female'),
                (27, 'Glen', 'Jesteco', 282775, 44.3, 'gjestecoq', 'Male'),
                (28, 'Sigmund', 'Beernaert', 717544, 47.0, 'sbeernaertr', 'Male'),
                (29, 'Brett', 'Ciementini', 730255, 92.2, 'bciementinis', 'Non-binary'),
                (30, 'Ingrid', 'Robillard', 807186, 79.2, 'irobillardt', 'Female'),
                (31, 'Molly', 'Acory', 929187, 52.6, 'macoryu', 'Female'),
                (32, 'Jacky', 'Shaul', 483968, 26.2, 'jshaulv', 'Male'),
                (33, 'Barret', 'Grunbaum', 573491, 83.7, 'bgrunbaumw', 'Male'),
                (34, 'Gauthier', 'Lane', 994187, 67.0, 'glanex', 'Male'),
                (35, 'Maximo', 'Simonini', 489965, 51.9, 'msimoniniy', 'Male'),
                (36, 'Modestine', 'Riggs', 113108, 98.6, 'mriggsz', 'Female'),
                (37, 'Annice', 'Kenwrick', 258938, 39.3, 'akenwrick10', 'Female'),
                (38, 'Gilli', 'Guyan', 227990, 73.5, 'gguyan11', 'Female'),
                (39, 'Gnni', 'Chrestien', 831913, 83.8, 'gchrestien12', 'Female'),
                (40, 'Hebert', 'Loblie', 709047, 10.7, 'hloblie13', 'Male'),
                (41, 'Addy', 'Goude', 542671, 5.5, 'agoude14', 'Male'),
                (42, 'Gibby', 'Chalcot', 772672, 13.0, 'gchalcot15', 'Male'),
                (43, 'Ruprecht', 'MacAnulty', 169565, 97.6, 'rmacanulty16', 'Male'),
                (44, 'Goddard', 'Boich', 588670, 85.4, 'gboich17', 'Male'),
                (45, 'Kai', 'McEntagart', 900293, 45.0, 'kmcentagart18', 'Female'),
                (46, 'Florence', 'Harry', 801029, 30.4, 'fharry19', 'Female'),
                (47, 'Maisie', 'Sandells', 119872, 86.3, 'msandells1a', 'Female'),
                (48, 'See', 'Hagley', 1036381, 28.6, 'shagley1b', 'Male'),
                (49, 'Son', 'Biddles', 172333, 47.5, 'sbiddles1c', 'Male'),
                (50, 'Malia', 'De Malchar', 406522, 32.7, 'mdemalchar1d', 'Genderqueer');

        """)
        self.mydb.commit()
    
    def selectData(self):
        self.cursor.execute("SELECT * FROM users WHERE (LENGTH(name) + LENGTH(surname)) > 10;")
        malumot = self.cursor.fetchall()
        return malumot
    
    def drop(self):
        self.cursor.execute("DROP TABLE users;")
        self.cursor.execute("DROP DATABASE users_data;")




db = Databaza()
lst = db.selectData()
for l in lst:
    print(f"{l[0]}-id egasi ma'lumotlari:\nISMI: {l[1]}\nFAMILIYASI: {l[2]}\nPAROLI: {l[3]}\nYOSHI: {l[4]}\nUSERNAME: {l[5]}\nJINSI: {l[6]}\n" )
db.drop()