import mysql.connector
import json
class user_model():
    def __init__(self):
        #connection establishment code
        try:
            self.con = mysql.connector.connect(host="localhost",username="root", password="" , database="flask_tutorial")
            self.con.autocommit = True
            self.cur=self.con.cursor(dictionary=True)
            print("connection successful")
        except:
            print("some error")

    def user_getall_model(self):
        #query execution code
        self.cur.execute("SELECT *FROM users")
        result = self.cur.fetchall()
        if len(result)>0:
            return json.dumps(result)
        else:
            return "No Data Found "
        
    def user_addone_model(self, data):
        #query execution code
        self.cur.execute(f"INSERT INTO users(name, email,phone,role,password) VALUES('{data['name']}', '{data['email']}','{data['phone']}','{data['role']}', '{data['password']}')")
        
        return "User Created Successfully"
    