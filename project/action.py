from conDB import Con
class Action:
    def getUser():
        data = Con.getUser()
        return data
    
    def login(user):
        user = Con.login(user)
        if user:
            data = {"error": False, "user": user}
            return data
        else:
            data = {"error": True}
            return data
    
    def SelectAll():
        data = Con.selectAll()
        return data
    
    def add_id_password(ID,password):
        ID = Con.addlogin(ID,password)
        data = Con.addlogin(ID,password)
        return data
