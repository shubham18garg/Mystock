import pymysql
import cgi
conn=pymysql.connect(host='localhost',user='root',password='1234',db='mystockmarket')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")
print("<html>")

res=cgi.FieldStorage()
cid=str(res.getvalue('cid'))
cnm=str(res.getvalue('cnm'))
cicon=str(res.getvalue('cicon'))
cdes=str(res.getvalue('cdes'))
btn=str(res.getvalue('btn'))
if btn=="Update":
	sql="update categoryreg set catname='"+str(cnm)+"', caticon='"+str(cicon)+"',catdesc='"+str(cdes)+"' where catid="+str(cid)
	insert=a.execute(sql)
	if insert!=0:
	    print("Record Updated Successfully...")
	else:
	    print("Record Not Updated Successfully...")
else:
	sql="delete from categoryreg where catid="+str(cid)
	insert=a.execute(sql)
	if insert!=0:
	    print("Record Deleted Successfully...")
	else:
	    print("Record Not Deleted Successfully...")

conn.commit()
