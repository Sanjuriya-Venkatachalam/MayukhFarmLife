#!C:\Python\python.exe
import cgi
import mysql.connector

print("Content-Type:text/html\r\n\r\n")

print("<html>")
print("<body style='background-color:#eddeb2;'>")
print("<h2>Thanks for submitting your message!</h2>")

Form = cgi.FieldStorage()
F_FName = Form.getvalue("FName")
F_LName = Form.getvalue("LName")
F_EmailID = Form.getvalue("EmailID")
F_Message = Form.getvalue("Message")

#print("<h1>", F_FName, F_LName, F_EmailID, F_Message, "</h1>")
print("<h3>We will contact you shortly via email.</h3>")
print("<a href='index.html' style='text-decoration:none; color: black;'>Back to home</a>")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Resort"
    )
mycursor = mydb.cursor()
Sql = "INSERT INTO messages(First_Name,Last_Name,Email_ID,Message)VALUES(%s,%s,%s,%s)";
Val = (F_FName, F_LName, F_EmailID, F_Message)
mycursor.execute(Sql,Val)
mycursor.close()
mydb.commit()
mydb.close()

print("</body>")
print("</html>")
