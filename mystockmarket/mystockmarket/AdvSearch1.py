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
	print("if<br>")
	sql="select * from categoryreg ca,companyreg co where ca.catid=co.catid"
elif catid=="None" and cnm!="None":
	print("elif1<br>")
	sql="select * from categoryreg ca,companyreg co where ca.catid=co.catid and comname like '%"+cnm+"%'"

elif catid!="None" and cnm=="None":
	print("elif2<br>")
	sql="select * from categoryreg ca,companyreg co where ca.catid=co.catid and ca.catid="+catid
else:
	print("else<br>")
	sql="select * from categoryreg ca,companyreg co where ca.catid=co.catid and comname like '%"+cnm+"%' and ca.catid="+catid

print(sql)

print("<head>")
print("<title>My Stock Market</title>")
print("</head>")
print("<body>")

print("<center>")
print("<table border=1>")
print("<tr><td>Category ID</td><td>Category Name</td><td>Company ID</td><td>Company Name</td><td>Company Image</td><td>Company Description</td><td>Company Website</td><td>Company IPO Price</td><td>Company IPO Date</td><td>-----</td></tr>")

display=a.execute(sql)
data=a.fetchall()
for i in data:
	print("<tr><td>"+str(i[0])+"</td><td>"+str(i[1])+"</td><td>"+str(i[5])+"</td><td>"+str(i[6])+"</td><td><img src="+str(i[7])+" height=100 width=100></td><td>"+str(i[8])+"</td><td><a href="+str(i[9])+" target=_blank>"+str(i[9])+"</a></td><td>"+str(i[10])+"</td><td>"+str(i[11])+"</td><td><a href=#>------</a></td></tr>")
print("</table>")
print("</center>")
print("</body>")
print("</html>")
