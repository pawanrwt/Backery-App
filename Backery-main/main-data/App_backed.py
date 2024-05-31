import mysql.connector
class Code():
    def __init__(self, master, **kwargs):
        self.master = master
        try:
            self.mydb = mysql.connector.Connect(
                host='localhost',
                user='root',
                password='YOUR PASSWORD',
                database='BACKERY'
            )
            self.cur = self.mydb.cursor()
            q1='''CREATE Table IF NOT EXISTS SIGNUP (
                USER VARCHAR(50) PRIMARY KEY,
                PASSWORD VARCHAR(15)
                )'''
            self.cur.execute(q1)
            self.mydb.commit()
            q2='''CREATE TABLE IF NOT EXISTS USER_DETAILS(
                username varchar(50),
                NAME VARCHAR(50),
                GENDER VARCHAR(7),
                DOB DATE,
                AGE INT,
                EMAIL_ID varchar(50) PRIMARY KEY,
                PHONE_NO VARCHAR(12),
                Address varchar(100),
                FAV_DISH VARCHAR(50)
                )'''
            self.cur.execute(q2)
            self.mydb.commit()
        except Exception:
            print("Exception : Make sure you are using SQL(Database) if not download the MySQL.")
            print("Exception : Also check your Host name, Username, Passwrod and Database")
    def Insertion(self,user,pas):
        try:
            if user:
                if pas:
                    self.cur.execute("INSERT INTO SIGNUP VALUES (%s,%s)",(user,pas))
                    self.mydb.commit()
                    print("Sign up successful")
                    return True
                else:
                    print("Enter password")
                    return False
            else:
                print("Enter user name")
                return "False2"
        except Exception as e:
            return 10

    def Check(self,user,pas):
        try:
            self.cur.execute("SELECT *FROM SIGNUP WHERE USER=%s",(user,))
            records=self.cur.fetchone()
            if records:
                uname=records[0]
                pasword=records[1]
            else: 
                return "False2"
            if uname and uname==user:
                
                if (pasword==pas and uname==user):
                    print("Login Successful")
                    return True
                else:
                    print("password is wrong")
                    return False
            else:
                print("User not found")
                return "False2"
        except Exception as e:
            print("Exception : ",e)
            return "server"
        
    def user_details(self,uname,gen,dob,age,em,ph,fd,add):
        try:
            with open ('store.txt','r+') as f:
                uid=f.read()
            if uname and gen and dob and em and ph and fd:
                self.cur.execute("INSERT INTO USER_DETAILS VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(uid,uname,gen,dob,age,em,ph,add,fd))
                self.mydb.commit()
                return True
            else:
                print("All box are neccessary to fill up")
                return False
        except Exception as e:
            print("Error : ",e)
            return 10
    def delsignup(self,uname):
        if uname:
            try:
                self.cur.execute("DELETE FROM SIGNUP WHERE USER=%s",(uname,))
                self.mydb.commit()
                print("sign up incomplete")
            except Exception as e:
                print("ERROR: ",e)
                        
    #update user details
    def editing(self, uname, gen, dob, age, em, ph, fd, add):
        try:
            with open('store.txt', 'r+') as f:
                uid = f.read()
            if uname and gen and dob and em and ph and fd:
                self.cur.execute("UPDATE USER_DETAILS SET NAME=%s, GENDER=%s, DOB=%s, AGE=%s, EMAIL_ID=%s, PHONE_NO=%s, ADDRESS=%s, FAV_DISH=%s WHERE USERNAME=%s",(uname, gen, dob, age, em, ph, add, fd, uid))
                self.mydb.commit()
                print("Updation Successful")
                return True
            else:
                self.cur.execute("SELECT *FROM USER_DETAILS WHERE USERNAME=%s",(uid,))
                records=self.cur.fetchone()
                if not uname:
                    uname=records[1]
                if not gen:
                    gen=records[2]
                if not dob:
                    dob=records[3]
                if not age:
                    age=records[4]
                if not em:
                    em=records[5]
                if not ph:
                    ph=records[6]
                if not add:
                    add=records[7]
                if not fd:
                    fd=records[8]
                self.cur.execute("UPDATE USER_DETAILS SET NAME=%s, GENDER=%s, DOB=%s, AGE=%s, EMAIL_ID=%s, PHONE_NO=%s, ADDRESS=%s, FAV_DISH=%s WHERE USERNAME=%s",(uname, gen, dob, age, em, ph, add, fd, uid))
                self.mydb.commit()
                print("Editing Successful")
                return True
        except Exception as e:
            print("Error: ", e)
            return False

    def userinfo(self):
        try:
            with open('store.txt','r+') as f:
                uid=f.read()
            self.cur.execute("SELECT NAME, PHONE_NO, Address FROM USER_DETAILS WHERE username = %s", (uid,))
            records = self.cur.fetchall()
            return records
        except Exception:
            print("user info has some server error")


    def logout(self,u_name):
        try:
            self.cur.execute("DELETE FROM USER_DETAILS WHERE USERNAME=%s",(u_name,))
            self.mydb.commit()
            self.cur.execute("DELETE FROM Signup WHERE USER=%s",(u_name,))
            self.mydb.commit()
            print("User deleted from server")
            return True
        except Exception as e:
            print("Exception : ",e)

    def records(self,user):
        try:
            self.cur.execute("SELECT *FROM USER_DETAILS WHERE USERNAME=%s",(user,))
            record=self.cur.fetchone()
            return record
        except Exception as e:
            print("Record not found")
            return record
