#!C:\Python\python.exe
import cgi
import mysql.connector

print("Content-Type:text/html\r\n\r\n")
print("<html>")
print("<body style='background-color:#eddeb2;'>")
print("<h2>Thanks for booking your room!</h2>")

Form = cgi.FieldStorage()
FCIN = Form.getvalue("CIN")
FR1 = Form.getvalue("room1")
FR2 = Form.getvalue("room2")
FR3 = Form.getvalue("room3")
FR4 = Form.getvalue("room4")
FD = Form.getvalue("noofdays")
InDate = Form.getvalue("checkindate")
OutDate = Form.getvalue("checkoutdate")
# print("<h1>", FCIN, FR1, FR2, FR3, FR4, FD, InDate, OutDate,"</h1>")
print("<h3>Thank You, Your room has been booked for,</h3>","<span>",FD,"</span>","<h3>days</h3>")

"""class Amount:
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
print("<h3>",Obj1.rent(FD, FR1, FR2, FR3, FR4),"</h3>")"""


#print("<h3>Your total room rent is, Rs</h3>")
print("<a href='index.html' style='text-decoration:none; color: black;'>Back to home</a>")

mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="resort"
	)

mycursor=mydb.cursor()

Sql="INSERT INTO room_booking(cid,ultraroyal,royal,elite,budget,days,checkin,checkout)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)";

Val = (FCIN, FR1, FR2, FR3, FR4, FD, InDate, OutDate)
mycursor.execute(Sql,Val)
mycursor.close()
mydb.commit()
mydb.close()


print("</body>")
print("</html>")
