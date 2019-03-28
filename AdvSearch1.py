import pymysql
import cgi
conn=pymysql.connect(host='localhost',user='root',password='1234',db='mystockmarket')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")
print("<html>")

res=cgi.FieldStorage()
catid=str(res.getvalue('catid'))
cnm=str(res.getvalue('cnm'))
print(catid+","+cnm+"<br>")

if catid=="None" and cnm=="None":
	print("if")
	sql="select * from categoryreg ca,companyreg co where ca.catid=co.catid"
elif catid=="None" and cnm!="None":
	print("elif1")
	sql="select * from categoryreg ca,companyreg co where ca.catid=co.catid and comname like %"+cnm+"%"

elif catid!="None" and cnm=="None":
	print("elif2")
	sql="select * from categoryreg ca,companyreg co where ca.catid=co.catid and ca.catid="+catid
else:
	print("else")
	sql="select * from categoryreg ca,companyreg co where ca.catid=co.catid and comname like %"+cnm+"% and ca.catid="+catid

print(sql)


