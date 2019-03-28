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
print("<center>")
print("<table border=1>")
print("<tr><td>Category ID</td><td>Category Name</td><td>Category Image</td><td>Category Description</td><td>Company Display</td></tr>")
sql="select * from categoryreg";
display=a.execute(sql)
data=a.fetchall()
for i in data:
	print("<tr><td>"+str(i[0])+"</td><td>"+str(i[1])+"</td><td><img src="+str(i[2])+" height=100 width=100></td><td>"+str(i[3])+"</td><td><a href=CompanyDisplay.py?catid="+str(i[0])+">Company Display</a></td></tr>")

print("</table>")
print("</center>")
print("</body>")
print("</html>")
