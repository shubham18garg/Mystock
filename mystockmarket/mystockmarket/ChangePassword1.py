import pymysql
import cgi
conn=pymysql.connect(host='localhost',user='root',password='1234',db='mystockmarket')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")
print("<html>")

res=cgi.FieldStorage()
lid=str(res.getvalue('lid'))
opwd=str(res.getvalue('opwd'))
npwd=str(res.getvalue('npwd'))
rnpwd=str(res.getvalue('rnpwd'))
f=0
if npwd == rnpwd:
	if opwd==npwd:
		print("<font size=5 color=red>Old password and New Password both are same</font>")
	else:
		q="select * from userreg where userlogin='"+lid+"' and userpwd='"+opwd+"'"
		display=a.execute(q)
		data=a.fetchall()
		for i in data:
			q="update userreg set userpwd='"+npwd+"' where userlogin='"+lid+"'";	
			res = a.execute(q)
			if res !=0:
				print("Password Changed...")
			else:
				print("Password Not Changed...")
			f=1
		if f==0:
			print("User ID / Password Not Matched...")
else:
	print("<font size=5 color=red>New Password are not Matched...</font>")
	
conn.commit()
