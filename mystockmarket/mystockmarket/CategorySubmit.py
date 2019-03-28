import pymysql
import cgi
conn=pymysql.connect(host='localhost',user='root',password='1234',db='mystockmarket')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")
print("<html>")

res=cgi.FieldStorage()
catname=str(res.getvalue('cname'))
cimg=str(res.getvalue('cimg'))
cdesc=str(res.getvalue('cdesc'))

sql="insert into categoryreg(catname,caticon,catdesc)values('"+catname+"','"+cimg+"','"+cdesc+"')"

insert=a.execute(sql)
if insert!=0:
    print("Record Inserted Successfully...")
else:
    print("failed")
conn.commit()
