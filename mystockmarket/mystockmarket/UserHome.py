import pymysql

import cgi
conn=pymysql.connect(host='localhost',user='root',password='1234',db='mystockmarket')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")
print("<html>")

res=cgi.FieldStorage()
ulid=str(res.getvalue('ulid'))
upwd=str(res.getvalue('upwd'))

sql="select * from userreg where userlogin='"+ulid+"' and userpwd='"+upwd+"'";
display=a.execute(sql)
data=a.fetchall()
for i in data:
	print("<html>")
	print("<head>")
	print("<title>My Stock Market</title>")
	print("</head>")
	print("<body>")
	print("<center>")
	print("<table border=0>")
	print("<caption><font size=7> User Home Page</font></caption>")
	print("<tr><td>Header</td><td><a href=UserLogin.py>Logout</a></td></tr>")
	print("<tr><td><a href=CategoryDisplay.py target=aa>Category Display</a><br>")
	print("<a href=CompanyDisplay.py target=aa>Company Display</a><br>")
	print("<a href=AdvSearch.py target=aa>Advance Search</a><br>")
	print("<a href=ChangePassword.py target=aa>Change Password</a><br>")
	print("</td><td><iframe src=AdvSearch.py name=aa height=800 width=800 frameborder=0></iframe></td></tr>")
	print("<tr><td>Footer</td><td>Footer</td></tr>")
	print("</table>")
	print("</center>")
	print("</form>")
	print("</body>")
	print("</html>")
else:
	print("ID / Password Not Matched...")
	print("<a href=UserLogin.py>Login Again</a>")
conn.commit()
