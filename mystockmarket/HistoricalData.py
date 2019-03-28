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
print("<tr><td>Date</td><td>ID</td><td>Company ID</td><td>Open Price</td><td>High Price</td><td>Low Price</td><td>Close Price</td><td>Price Change</td><td>Per</td><td>Volume</td></tr>")
try:
	res=cgi.FieldStorage()
	comid=str(res.getvalue('comid'))
	sql="select * from compri where comid='"+comid+"'";

except:
	print("Error...")


print(sql)
display=a.execute(sql)
data=a.fetchall()
for i in data:
	print("<tr><td>"+str(i[7])+"</td><td>"+str(i[0])+"</td><td>"+str(i[1])+"</td><td>"+str(i[2])+"</td><td>"+str(i[3])+"</td><td>"+str(i[4])+"</td><td>"+str(i[5])+"</td>")
	oc=int(i[5])-int(i[2])
	per=(oc/int(i[5]))*100
	if oc>0:
		print("<td><font color=green>"+str(oc)+"</font></td><td><font color=green>"+str(per)+"</font></td>")
	elif oc<0:
		print("<td><font color=red>"+str(oc)+"</font></td><td><font color=red>"+str(per)+"</font></td>")
	else:
		print("<td>"+str(oc)+"</td><td>"+str(per)+"</td>")
	
	print("<td>"+str(i[6])+"</td></tr>")
print("</table>")
print("</center>")
print("</body>")
print("</html>")
