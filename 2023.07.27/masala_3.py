import mysql.connector
import datetime
from os import system

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
        self.insertData()

    def dbConnection(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS najot_talim;")
        self.cursor.execute("USE najot_talim;")


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
            insert into users (id, name, surname, password, age, username, gender) values 
                (1, 'Thaddeus', 'Read', 598233, 27, 'tread0', 'Male'),
                (2, 'Ingelbert', 'Duckinfield', 938213, 33, 'iduckinfield1', 'Male'),
                (3, 'Fionnula', 'Spire', 928619, 70, 'fspire2', 'Female'),
                (4, 'Maurine', 'Follitt', 1050819, 43, 'mfollitt3', 'Female'),
                (5, 'Cob', 'Northall', 587228, 32, 'cnorthall4', 'Male'),
                (6, 'Bailie', 'Vivians', 804596, 69, 'bvivians5', 'Male'),
                (7, 'Lennard', 'Maharey', 535853, 17, 'lmaharey6', 'Male'),
                (8, 'Melicent', 'Segebrecht', 801653, 23, 'msegebrecht7', 'Female'),
                (9, 'Gabe', 'Jerrold', 960583, 35, 'gjerrold8', 'Male'),
                (10, 'Katina', 'Tebbs', 674519, 46, 'ktebbs9', 'Female'),
                (11, 'Rafe', 'Heistermann', 154776, 41, 'rheistermanna', 'Polygender'),
                (12, 'Birdie', 'Truelove', 1078137, 17, 'btrueloveb', 'Genderqueer'),
                (13, 'Archibold', 'Forbes', 140050, 26, 'aforbesc', 'Male'),
                (14, 'Tanner', 'Hamerton', 880680, 91, 'thamertond', 'Male'),
                (15, 'Amalle', 'Riddich', 248183, 97, 'ariddiche', 'Female'),
                (16, 'Zonda', 'Green', 374148, 27, 'zgreenf', 'Female'),
                (17, 'Forster', 'Lancett', 819079, 46, 'flancettg', 'Non-binary'),
                (18, 'Renelle', 'Speerman', 457158, 72, 'rspeermanh', 'Female'),
                (19, 'Aldon', 'Pervoe', 456336, 46, 'apervoei', 'Male'),
                (20, 'Willem', 'Aidler', 865413, 90, 'waidlerj', 'Male'),
                (21, 'Dorie', 'Mongain', 672294, 81, 'dmongaink', 'Male'),
                (22, 'Mufinella', 'Kyncl', 921351, 49, 'mkyncll', 'Female'),
                (23, 'Arleyne', 'Daville', 769493, 47, 'adavillem', 'Female'),
                (24, 'Dwight', 'Rives', 658503, 56, 'drivesn', 'Male'),
                (25, 'Nata', 'Vasilyev', 625178, 38, 'nvasilyevo', 'Non-binary'),
                (26, 'Alexandrina', 'Cottrell', 180514, 17, 'acottrellp', 'Female'),
                (27, 'Glen', 'Jesteco', 282775, 44, 'gjestecoq', 'Male'),
                (28, 'Sigmund', 'Beernaert', 717544, 47, 'sbeernaertr', 'Male'),
                (29, 'Brett', 'Ciementini', 730255, 92, 'bciementinis', 'Non-binary'),
                (30, 'Ingrid', 'Robillard', 807186, 79, 'irobillardt', 'Female'),
                (31, 'Molly', 'Acory', 929187, 52, 'macoryu', 'Female'),
                (32, 'Jacky', 'Shaul', 483968, 26, 'jshaulv', 'Male'),
                (33, 'Barret', 'Grunbaum', 573491, 83, 'bgrunbaumw', 'Male'),
                (34, 'Gauthier', 'Lane', 994187, 67, 'glanex', 'Male'),
                (35, 'Maximo', 'Simonini', 489965, 51, 'msimoniniy', 'Male'),
                (36, 'Modestine', 'Riggs', 113108, 98, 'mriggsz', 'Female'),
                (37, 'Annice', 'Kenwrick', 258938, 39, 'akenwrick10', 'Female'),
                (38, 'Gilli', 'Guyan', 227990, 73, 'gguyan11', 'Female'),
                (39, 'Gnni', 'Chrestien', 831913, 83, 'gchrestien12', 'Female'),
                (40, 'Hebert', 'Loblie', 709047, 10, 'hloblie13', 'Male'),
                (41, 'Addy', 'Goude', 542671, 14, 'agoude14', 'Male'),
                (42, 'Gibby', 'Chalcot', 772672, 17, 'gchalcot15', 'Male'),
                (43, 'Ruprecht', 'MacAnulty', 169565, 97, 'rmacanulty16', 'Male'),
                (44, 'Goddard', 'Boich', 588670, 85, 'gboich17', 'Male'),
                (45, 'Kai', 'McEntagart', 900293, 45, 'kmcentagart18', 'Female'),
                (46, 'Florence', 'Harry', 801029, 30, 'fharry19', 'Female'),
                (47, 'Maisie', 'Sandells', 119872, 86, 'msandells1a', 'Female'),
                (48, 'See', 'Hagley', 1036381, 28, 'shagley1b', 'Male'),
                (49, 'Son', 'Biddles', 172333, 47, 'sbiddles1c', 'Male'),
                (50, 'Malia', 'De Malchar', 406522, 32, 'mdemalchar1d', 'Genderqueer');

        """)
        self.mydb.commit()
    
    def selectData(self):
        self.cursor.execute("SELECT * FROM users;")
        malumot = self.cursor.fetchall()
        return malumot
    
    def updateData(self, new_password):
        self.cursor.execute(f"UPDATE users SET password = {new_password} WHERE 1 = 1")
    
    def deleteData(self, id):
        self.cursor.execute(f"DELETE FROM users WHERE id = '{id}'")
    
    def drop(self):
        self.cursor.execute("DROP TABLE users;")
        self.cursor.execute("DROP DATABASE najot_talim;")

def tupleToDict(lst: tuple) -> dict:
    dt = dict()
    dt['id'] = lst[0]
    dt['name'] = lst[1]
    dt['surname'] = lst[2]
    dt['password'] = lst[3]
    dt['age'] = lst[4]
    dt['username'] = lst[5]
    dt['gender'] = lst[6]
    return dt


db = Databaza()
lst = db.selectData()

# 1 - shart
# for l in lst:
#     user = tupleToDict(l)
#     if user['age'] > 15 and user['age'] < 30:
#         print(f"{user['id']}-id egasi ma'lumotlari:\nISMI: {user['name']}\nFAMILIYASI: {user['surname']}\nPAROLI: {user['password']}\nYOSHI: {user['age']}\nUSERNAME: {user['username']}\nJINSI: {user['gender']}\n" )

# 2 - shart
# count = 0
# for l in lst:
#     user = tupleToDict(l)
#     if user['age'] == 17:
#         count += 1
# print(count)

# 3 - shart
# for l in lst:
#     user = tupleToDict(l)
#     if list(user['name'])[0] == 'A':
#         print(f"{user['id']}-id egasi ma'lumotlari:\nISMI: {user['name']}\nFAMILIYASI: {user['surname']}\nPAROLI: {user['password']}\nYOSHI: {user['age']}\nUSERNAME: {user['username']}\nJINSI: {user['gender']}\n" )

# 4 - shart
# for l in lst:
#     user = tupleToDict(l)
#     if user['gender'].lower() == 'female':
#         print(f"{user['id']}-id egasi ma'lumotlari:\nISMI: {user['name']}\nFAMILIYASI: {user['surname']}\nPAROLI: {user['password']}\nYOSHI: {user['age']}\nUSERNAME: {user['username']}\nJINSI: {user['gender']}\n" )

# 5 - shart
# for l in lst:
#     user = tupleToDict(l)
#     if user['name'] == 'Ali' or user['name'] == 'Abror' or user['name'] == 'Gulnoza':
#         print(f"{user['id']}-id egasi ma'lumotlari:\nISMI: {user['name']}\nFAMILIYASI: {user['surname']}\nPAROLI: {user['password']}\nYOSHI: {user['age']}\nUSERNAME: {user['username']}\nJINSI: {user['gender']}\n" )

# 6 - shart
# for l in lst:
#     user = tupleToDict(l)
#     if user['gender'].lower() == 'female':
#         db.deleteData(user['id'])

# 7 - shart
# old_user = tupleToDict(lst[0])
# for l in lst:
#     user = tupleToDict(l)
#     if user['age'] > old_user['age'] and user['gender'].lower() == 'male':
#         old_user = user
# print(f"Eng yoshi katta erkak ma'lumotlari:\nISMI: {old_user['name']}\nFAMILIYASI: {old_user['surname']}\nPAROLI: {old_user['password']}\nYOSHI: {old_user['age']}\nUSERNAME: {old_user['username']}\nJINSI: {old_user['gender']}\n" )

# 8 - shart
# for l in lst:
#     user = tupleToDict(l)
#     if user['name'] == 'Abror' or user['name'] == 'Gulnoza':
#         db.updateData("qwer1234")


db.drop()