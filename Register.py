#!C:\Python\python.exe

import cgi
import mysql.connector
# import sys
# import os

# Add the current working directory to the Python path
# sys.path.append(os.getcwd())

print("Content-Type:text/html\r\n\r\n")

print("<html>")
print("<body style='background-color:#eddeb2;text-align:center;'>")
print("<h2>Thank You For Registering Your Details.</h2>")

form = cgi.FieldStorage()
global FCIN 
FCIN = form.getvalue("CIN")
FCName = form.getvalue("CName")
FCAddr = form.getvalue("CAddr")
FCAge = form.getvalue("CAge")
FCCountry = form.getvalue("CCountry")
FCPhNo = form.getvalue("CPhNo")
FCMailID = form.getvalue("CMailID")

# print("<h1>", FCIN, FCName, FCAddr, FCAge, FCCountry, FCPhNo, FCMailID, "</h1>")

print("<a href='rooms.html' style='color: red;letter-spacing: 1.2px;'>Click here for room booking!</a>")
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="Resort"
	)

mycursor = mydb.cursor()

Sql = "INSERT INTO c_details(c_id,c_name,c_address,c_age,c_country,c_phno,c_email)VALUES(%s,%s,%s,%s,%s,%s,%s)";
Val = (FCIN, FCName, FCAddr, FCAge, FCCountry, FCPhNo, FCMailID)
mycursor.execute(Sql,Val)
mycursor.close()
mydb.commit()
mydb.close()

print("</body>")
print("</html>")
