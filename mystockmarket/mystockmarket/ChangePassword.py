import pymysql
import cgi

conn=pymysql.connect(host='localhost',user='root',password='1234',db='mystockmarket')
a=conn.cursor()

print("content-text:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>My Stock Market</title>")
print("</head>")
print("<body>")
print("<form action=ChangePassword1.py>")
print("<center>")
print("<table border=1>")
print("<caption><font size=7>Change Password</font></caption>")
print("<tr><td>Enter Login ID</td><td><input type=text name=lid></td></tr>")
print("<tr><td>Enter Old Password</td><td><input type=password name=opwd></td></tr>")
print("<tr><td>Enter New Password</td><td><input type=password name=npwd></td></tr>")
print("<tr><td>Re-enter New Password</td><td><input type=password name=rnpwd></td></tr>")
print("<tr><td><input type=submit value=\"Change Password\"></td><td><input type= reset></td></tr>")
print("</table>")
print("</center>")
print("</form>")

print("</body>")
print("</html>")
