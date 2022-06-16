import mysql.connector

def con():
    mydb = mysql.connector.connect(
        host="localhost",
        user="project",
        password="1234",
        database="project",
    )
    return mydb


class Con:
    def getHW():
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "SELECT * FROM user"

        mycursor.execute(sql)

        data = mycursor.fetchall()

        mycursor.close()

        mydb.close()

        return data

    def getHWByID(ID):
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "SELECT * FROM user WHERE id = {}".format(ID)

        mycursor.execute(sql)

        data = mycursor.fetchall()

        mycursor.close()

        mydb.close()

        return data

    def getHWByName(name):
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "SELECT * FROM user WHERE name = '{}'".format(name)

        mycursor.execute(sql)

        data = mycursor.fetchall()

        mycursor.close()

        mydb.close()

        return data

    def addHW(name, hw_name):
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "INSERT INTO user (name, hw_name, status, value) VALUES ('{}', '{}','OFF',0.00)".format(
            name, hw_name
        )

        mycursor.execute(sql)

        mydb.commit()

        mycursor.close()

        mydb.close()

        ID = mycursor.lastrowid

        return ID

    def updateStatusHW(ID, status):
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "UPDATE hard_ware SET status = '{}' WHERE id = {}".format(status, ID)

        mycursor.execute(sql)

        mydb.commit()

        mycursor.close()

        mydb.close()

        return True

    def updateValueHW(ID, value):
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "UPDATE hard_ware SET value = {} WHERE id = {}".format(value, ID)

        mycursor.execute(sql)

        mydb.commit()

        mycursor.close()

        mydb.close()

        return True

    def DeleteHW(ID):
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "DELETE FROM user WHERE id = {}".format(ID)

        mycursor.execute(sql)

        mydb.commit()

        mycursor.close()

        mydb.close()

        return True


class Con2:
    def login(user):
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "SELECT * FROM user WHERE name = '{}' and password = '{}'".format(user.username, user.password)

        mycursor.execute(sql)

        data = mycursor.fetchall()

        mycursor.close()

        mydb.close()

        return data

    def getUser(ID):
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "SELECT * FROM user WHERE id = {}".format(ID)

        mycursor.execute(sql)

        data = mycursor.fetchall()

        mycursor.close()

        mydb.close()

        return data


    def register(user):
        
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "INSERT INTO user (username, password, name, last_name, address) VALUES ('{}', '{}', '{}', '{}', '{}')".format(user.username, user.password, user.name, user.last_name, user.address)

        mycursor.execute(sql)

        mydb.commit()

        mycursor.close()

        mydb.close()

        ID = mycursor.lastrowid

        return ID

    def checkUserForRegister(username):
        
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "SELECT username FROM user WHERE username = '{}'".format(username)

        mycursor.execute(sql)

        data = mycursor.fetchall()

        mycursor.close()

        mydb.close()

        return data

    
    def changePassword(user):
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "UPDATE user SET password = '{}' WHERE id = {}".format(user.password,user.ID)

        mycursor.execute(sql)

        mydb.commit()

        mycursor.close()

        mydb.close()

        return True
    
    def deleteUser(user):
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "DELETE FROM user WHERE id = {}".format(user.ID)

        mycursor.execute(sql)

        mydb.commit()

        mycursor.close()

        mydb.close()

        return True