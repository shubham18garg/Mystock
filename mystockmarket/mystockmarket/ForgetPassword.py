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
print("<form action=ForgetPassword1.py>")
print("<center>")
print("<table border=1>")
print("<caption><font size=7> Forget Password</font></caption>")
print("<tr><td>Enter Login ID</td><td><input type=text name=lid></td></tr>")
print("<tr><td>Enter Email ID</td><td><input type=email name=eid></td></tr>")
print("<tr><td><input type=submit value=\"Get Password\"></td><td><input type= reset></td></tr>")
print("</table>")
print("</center>")
print("</form>")

print("<center>")
print("<table border=1>")
print("<tr><td>Category ID</td><td>Category Name</td><td>Category Image</td><td>Category Description</td><td>update/delete</td></tr>")
sql="select * from categoryreg";
display=a.execute(sql)
data=a.fetchall()
for i in data:
	print("<tr><td>"+str(i[0])+"</td><td>"+str(i[1])+"</td><td><img src="+str(i[2])+" height=100 width=100></td><td>"+str(i[3])+"</td><td><a href=CategoryUpDe.py?catid="+str(i[0])+">update/delete</a></td></tr>")

print("</table>")
print("</center>")
print("</body>")
print("</html>")
