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
    def addlogin(id,password):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "INSERT INTO login (id,password) VALUES ('{}', '{}')".format (id,password)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        data = mycursor.lastrowid
        return data
    
    def selectAll():
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM login"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data

    def login(user):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM user WHERE name = '{}' and password = '{}'".format(user.username, user.password)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data

    # def Forgot_Password():
    #     mydb = con()
    #     mycursor = mydb.cursor(dictionary=True)
    #     sql = "SELECT * FROM user WHERE name = '{}' and password = '{}'".format(username,password)
    #     mycursor.execute(sql)
    #     data = mycursor.fetchall()
    #     mycursor.close()
    #     mydb.close()
    #     return data
