#!C:\Python\python.exe

import cgi
import mysql.connector

print("Content-Type:text/html\r\n\r\n")
print("<html>")
print("<body style='background-color:#eddeb2;text-align:center;'>")
Form = cgi.FieldStorage()
FCIN = Form.getvalue("CIN")
FR1 = Form.getvalue("room1")
FR2 = Form.getvalue("room2")
FR3 = Form.getvalue("room3")
FR4 = Form.getvalue("room4")
FDays = int(Form.getvalue("noofdays"))
FInDate = Form.getvalue("checkindate")
FOutDate = Form.getvalue("checkoutdate")
# print("<h1>",FCIN,FR1,FR2,FR3,FR4,FDays,FInDate,FOutDate,"</h1>")
print("<div style='display:flex;justify-content:center;font-weight:bold;font-size:1.2em;'>","<p>Thank You, Your Room Has Been Booked For : </p>","<p style='color:#165e58;'>",FDays,"</p>","<p>Days</p>","</div>")
# Calculating room rent
class Amount:
    def rent(self,DAYS = 0, R1 = None, R2 = None, R3 = None, R4 = None):
        A1=10000
        A2=5000
        A3=3500
        A4=2500
        if DAYS!=None and R1!=None and R2!=None and R3!=None and R4!=None:
            result = (A1+A2+A3+A4) * DAYS
        elif R1!=None and R2!=None and R3!=None and DAYS!=None:
            result = (A1+A2+A3) * DAYS
        elif R1!=None and R2!=None and R4!=None and DAYS!=None:
            result = (A1+A2+A4) * DAYS
        elif R1!=None and R3!=None and R4!=None and DAYS!=None:
            result = (A1+A3+A4) * DAYS
        elif R2!=None and R3!=None and R4!=None and DAYS!=None:
            result = (A2+A3+A4) * DAYS
        elif R1!=None and R2!=None and DAYS!=None:
            result = (A1+A2) * DAYS
        elif R1!=None and R3!=None and DAYS!=None:
            result = (A1+A3) * DAYS
        elif R1!=None and R4!=None and DAYS!=None:
            result = (A1+A4) * DAYS
        elif R2!=None and R3!=None and DAYS!=None:
            result = (A2+A3) * DAYS
        elif R2!=None and R4!=None and DAYS!=None:
            result = (A2+A4) * DAYS
        elif R3!=None and R4!=None and DAYS!=None:
            result = (A3+A4) * DAYS
        elif R1!=None and DAYS!=None:
            result = (A1) * DAYS
        elif R2!=None and DAYS!=None:
            result = (A2) * DAYS
        elif R3!=None and DAYS!=None:
            result = (A3) * DAYS
        elif R4!=None and DAYS!=None:
            result = (A4) * DAYS
        else:
            result = 0
        return result
Obj1 = Amount()
# print("<h3>",Obj1.rent(FDays, FR1, FR2, FR3, FR4),"</h3>")
print("<div style='display:flex;justify-content:center;font-weight:bold;font-size:1.2em;'>","<p>Your Total Room Rent is : Rs.</p>","<p>",Obj1.rent(FDays, FR1, FR2, FR3, FR4),"</p>","</div>")
print("<p style='font-weight:bold;'>Thank You, Visit Mayukh Farm Life!</p>")
print("<a href='/MayukhFarmHouse' style='letter-spacing: 0.6px;font-size:0.9em;'>Back To Home</a>")
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Resort"
)
mycursor=mydb.cursor()
Sql="INSERT INTO room_booking(cid,ultraroyal,royal,elite,budget,days,checkin,checkout,bill_amt)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)";
Val=(FCIN,FR1,FR2,FR3,FR4,FDays,FInDate,FOutDate,Obj1.rent(FDays, FR1, FR2, FR3, FR4))

mycursor.execute(Sql,Val)
mydb.commit()
print("</body>")
print("</html>")
