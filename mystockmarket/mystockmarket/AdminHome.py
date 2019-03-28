import pymysql

import cgi
conn=pymysql.connect(host='localhost',user='root',password='1234',db='mystockmarket')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")
print("<html>")

res=cgi.FieldStorage()
lid=str(res.getvalue('lid'))
pwd=str(res.getvalue('pwd'))

if lid=="admin" and pwd=="admin":
	print("<html>")
	print("<head>")
	print("<title>My Stock Market</title>")
	print("</head>")
	print("<body>")
	print("<center>")
	print("<table border=0>")
	print("<caption><font size=7> Admin Home Page</font></caption>")
	print("<tr><td>Header</td><td>Header</td></tr>")
	print("<tr><td><a href=CategoryInterface.py target=aa>Category Form</a><br>")
	print("<a href=CompanyInterface.py target=aa>Company Form</a><br>")
	print("</td><td><iframe src=CategoryInterface.py name=aa height=800 width=800 frameborder=0></iframe></td></tr>")
	print("<tr><td>Footer</td><td>Footer</td></tr>")
	print("</table>")
	print("</center>")
	print("</form>")
	print("</body>")
	print("</html>")
else:
	print("ID / Password Not Matched...")
conn.commit()
