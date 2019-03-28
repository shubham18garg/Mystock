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
print("<form action=CategorySubmit.py>")
print("<center>")
print("<table border=1>")
print("<caption><font size=7> Stock Category Registration </font></caption>")
print("<tr><td>Enter Category Name</td><td><input type=text name=cname></td></tr>")
print("<tr><td>Upload Category Image</td><td><input type= file name=cimg></td></tr>")
print("<tr><td>Enter Category Description</td><td><textarea name=cdesc rows=4 cols=30></textarea></td></tr>")
print("<tr><td><input type=submit></td><td><input type= reset></td></tr>")
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
