import pymysql
import cgi
conn=pymysql.connect(host='localhost',user='root',password='1234',db='mystockmarket')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")
print("<html>")

res=cgi.FieldStorage()
ufnm=str(res.getvalue('ufnm'))
ulnm=str(res.getvalue('ulnm'))
dob=str(res.getvalue('dob'))
g=str(res.getvalue('g'))
umno=str(res.getvalue('umno'))
ueid=str(res.getvalue('ueid'))
ano=str(res.getvalue('ano'))
ac=str(res.getvalue('ac'))
ph=str(res.getvalue('ph'))
sign=str(res.getvalue('sign'))



sql="insert into userreg (username,userdob,usergen,usermob,useremail,useraadhar,useraadharph,userphoto,usersign,userlogin,userpwd)values('"+ufnm+" "+ulnm+"','"+dob+"','"+g+"','"+umno+"','"+ueid+"','"+ano+"','"+ac+"','"+ph+"','"+sign+"','"+ufnm+ano+"','"+ulnm+umno+"')"



insert=a.execute(sql)
if insert!=0:
    print("Record Inserted Successfully...")
else:
    print("failed")
conn.commit()
