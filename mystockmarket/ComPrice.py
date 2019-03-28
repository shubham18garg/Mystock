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
print("<table border=0>")
try:
	res=cgi.FieldStorage()
	comid=str(res.getvalue('comid'))
	sql="select * from categoryreg ca,companyreg co where ca.catid=co.catid and co.comid='"+comid+"'";
except:
	print("Error...")


print(sql)
display=a.execute(sql)
data=a.fetchall()
for i in data:
	print("<tr><td><img src="+str(i[7])+" height=100 width=100></td><td><font size=5 color=green face=monotype corsiva>"+str(i[6])+"(<i>ID: </i>"+str(i[5])+")</font><br>Category:"+str(i[2])+"("+str(i[1])+")</td><td>IPO Price: "+str(i[10])+"<br>Date: "+str(i[11])+"</td><td><a href="+str(i[9])+" target=_blank>"+str(i[9])+"</a><br><br><a href=HistoricalData.py?comid="+str(i[5])+" target=aaa>Historical Data</a></td></tr>")

print("<tr><td colspan=4><iframe name=aaa height=600 width=600 frameborder=0></iframe><td></tr>")
print("</table>")
print("</center>")
print("</body>")
print("</html>")
