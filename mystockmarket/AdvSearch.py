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
print("<form action=AdvSearch1.py>")
print("<center>")
print("<table border=1>")
print("<tr><td>")
# fill dropdown from database
print("<select name=catid>")
sql="select * from categoryreg";
display=a.execute(sql)
data=a.fetchall()
print("<option value=\"\">-Select Category Name-</option>")
for i in data:
	print("<option value="+str(i[0])+">"+str(i[1])+"</option>")

print("</select>")
# end

print("</td><td><input type=text name=cnm placeholder=\"Enter Company Name\"></td>")
print("<td><input type=submit value=Search></td></tr>")
print("<tr><td colspan=3><iframe src=AdvSearch1.py name=aa height=500 width=500 frameborder=0></td></tr>")

print("</table>")
print("</center>")
print("</form>")
print("</body>")
print("</html>")
