import mysql.connector
class transfers:
    def __init__(self):
        pass
    def dotransfer(self):
        try:
            conn=mysql.connector.connect(host='govtbot-db.ciymeoyjtgul.us-east-1.rds.amazonaws.com',
                                         database='Governmentbotdb',
                                         user='admin',password='shiva123')
            sql="select id,title,shortname,description,link from unverifiedsites"
            cursor=conn.cursor()
            cursor.execute(sql)
            records=cursor.fetchall()
            for row in records:
                title=row[1]
                shortname=row[2]
                desc=row[3]
                link=row[4]
                print(title)
                print(shortname)
                print(desc)
                print(link)
                if("https" in link and ".in" in link):
                    sql="insert into verifiedsites (title,shortname,description,link) values(%s,%s,%s,%s)"
                    args=(title,shortname,desc,link)
                    cursor.execute(sql,args)
                    conn.commit()
            #sql="truncate table unverifiedsites"
            #cursor.execute(sql)
            #conn.commit()
            sql="select id,vtitle,vstitle,vdesc,vlink from unverifiedvideo"
            cursor=conn.cursor()
            cursor.execute(sql)
            records=cursor.fetchall()
            for row in records:
                title=row[1]
                shortname=row[2]
                desc=row[3]
                link=row[4]
                print(title)
                print(shortname)
                print(desc)
                print(link)
                if("https" in link):
                    sql="insert into verifiedvideo (vtitle,vstitle,vdesc,vlink) values(%s,%s,%s,%s)"
                    args=(title,shortname,desc,link)
                    cursor.execute(sql,args)
                    conn.commit()
            #sql="truncate table unverifiedvideo"
            #cursor.execute(sql)
            #conn.commit()
            return True   
        except:
            print("exception occured")  
            return False      
#trans=transfers()
#print(trans.dotransfer())