import pymysql
import cgi
conn=pymysql.connect(host='localhost',user='root',password='1234',db='mystockmarket')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")
print("<html>")

res=cgi.FieldStorage()
catid=str(res.getvalue('cid'))
coid=str(res.getvalue('coid'))
coname=str(res.getvalue('coname'))
coimg=str(res.getvalue('coimg'))
codesc=str(res.getvalue('codesc'))
coweb=str(res.getvalue('coweb'))
ipop=str(res.getvalue('ipop'))
ipod=str(res.getvalue('ipod'))

sql="insert into companyreg(catid,comid,comname,comicon,comdesc,comweb,comipop,comipod)values("+catid+",'"+coid+"','"+coname+"','"+coimg+"','"+codesc+"','"+coweb+"','"+ipop+"','"+ipod+"')"

insert=a.execute(sql)
if insert!=0:
    print("Record Inserted Successfully...")
else:
    print("failed")
conn.commit()
