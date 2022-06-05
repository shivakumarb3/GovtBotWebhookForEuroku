import mysql.connector
class connector:
    e1=None
    e2=None
    i=None
    connection=None
    def __init__(self,intent,entity1,q,entity2=None):
        self.e1 = entity1
        self.i=intent
        self.e2=entity2
        self.query=q
        self.connection = mysql.connector.connect(host='govtbot-db.ciymeoyjtgul.us-east-1.rds.amazonaws.com',
                                         database='Governmentbotdb',
                                         user='admin',password='shiva123')
    def getsitelink(self):
        site="nope"
        res=""
        title=""
        if(self.e2!=None):
            #print( self.e2+" "+self.e1+" site will be given soon")
            sql_select_Query="select link,title from verifiedsites where title like %s or title like %s"
            cursor=self.connection.cursor()
            res=self.e2+" "+self.e1+" application"
            res2=self.e1+" application"
            args=['%'+res+'%',res2+'%']
            cursor.execute(sql_select_Query,args)
            records=cursor.fetchall()
            if len(records)==0:
                return self.findanswer(0)
            for row in records:
                site=row[0]
                title=row[1]
                break
        else:
            #print(self.e1)
            sql_select_Query="select link,title from verifiedsites where title like %s"
            cursor=self.connection.cursor()
            res=self.e1+" application"
            args=['%'+res+'%']
            cursor.execute(sql_select_Query,args)
            records=cursor.fetchall()
            #print(len(records))
            if len(records)==0:
                return self.findanswer(0)
            for row in records:
                site=row[0]
                title=row[1]
                break
        if site=="nope":
            return " "
        if(self.connection.is_connected()):
            sql_select_Query = "select count from shownsites where sitelink=%s"
            args=[site]
            cursor=self.connection.cursor()
            cursor.execute(sql_select_Query,args)
            records=cursor.fetchall()
            c=1
            #print(len(records))
            if(len(records)>0):
                #print("updating")
                for row in records:
                    c=row[0]+1
                    break
                sql_select_Query = "update shownsites set count=%s,title=%s where sitelink=%s"
                args=[c,title,site]
                cursor.execute(sql_select_Query,args)
                self.connection.commit()
            else:
                #print("new insert")
                sql_select_Query = "insert into shownsites(sitelink,count,title) values(%s,%s,%s)"
                recordTuple = (site,1,title)
                cursor.execute(sql_select_Query,recordTuple)
                self.connection.commit()
        #print(self.i+" "+self.e1)
        return site
    def getyoutubelink(self):
        site="nope"
        res=""
        title=""
        if(self.e2!=None):
            #print( self.e2+" "+self.e1+" video link will be given soon")
            sql_select_Query="select vlink,vtitle from verifiedvideo where vtitle like %s or vtitle like %s"
            cursor=self.connection.cursor()
            res="how to apply for "+self.e1+" in "+self.e2
            res2="how to apply for "+self.e1
            args=[res,res2]
            cursor.execute(sql_select_Query,args)
            records=cursor.fetchall()
            #print(len(records))
            if len(records)==0:
                return self.findanswer(1)
            for row in records:
                site=row[0]
                title=row[1]
                break
        else:
            #print(self.e1)
            sql_select_Query="select vlink,vtitle from verifiedvideo where vtitle like %s"
            cursor=self.connection.cursor()
            res="how to apply for "+self.e1
            args=[res+'%']
            cursor.execute(sql_select_Query,args)
            records=cursor.fetchall()
            #print(len(records))
            if len(records)==0:
                return self.findanswer(1)
            for row in records:
                site=row[0]
                title=row[1]
                break
        if site=="nope":
            return " "
        if(self.connection.is_connected()):
            sql_select_Query = "select count from shownvideos where sitelink=%s"
            args=[site]
            cursor=self.connection.cursor()
            cursor.execute(sql_select_Query,args)
            records=cursor.fetchall()
            c=1
            #print(len(records))
            if(len(records)>0):
                #print("updating")
                for row in records:
                    c=row[0]+1
                    break
                sql_select_Query = "update shownvideos set count=%s,title=%s where sitelink=%s"
                args=[c,title,site]
                cursor.execute(sql_select_Query,args)
                self.connection.commit()
            else:
                #print("new insert")
                sql_select_Query = "insert into shownvideos(sitelink,count,title) values(%s,%s,%s)"
                recordTuple = (site,1,title)
                cursor.execute(sql_select_Query,recordTuple)
                self.connection.commit()
        #print(self.i+" "+self.e1)
        return site
    def findanswer(self,type):
        site="nope"
        if(type==0):
            sql_select_Query="select link,title from verifiedsites where title like %s or shortname like %s or description like %s"
            cursor=self.connection.cursor()
            args=['%'+self.query+'%','%'+self.query+'%','%'+self.query+'%']
            cursor.execute(sql_select_Query,args)
            records=cursor.fetchall()
            for row in records:
                site=row[0]
                title=row[1]
                break
            if(site=="nope"):
                return "nope"
            sql_select_Query = "select count from shownsites where sitelink=%s"
            args=[site]
            cursor=self.connection.cursor()
            cursor.execute(sql_select_Query,args)
            records=cursor.fetchall()
            c=1
            #print(len(records))
            if(len(records)>0):
                #print("updating")
                for row in records:
                    c=row[0]+1
                    break
                sql_select_Query = "update shownsites set count=%s,title=%s where sitelink=%s"
                args=[c,title,site]
                cursor.execute(sql_select_Query,args)
                self.connection.commit()
            else:
                #print("new insert")
                sql_select_Query = "insert into shownsites(sitelink,count,title) values(%s,%s,%s)"
                recordTuple = (site,1,title)
                cursor.execute(sql_select_Query,recordTuple)
                self.connection.commit()
            return site
        else:
            sql_select_Query="select vlink,vtitle from verifiedvideo where vtitle like %s or vstitle like %s or vdesc like %s"
            cursor=self.connection.cursor()
            args=['%'+self.query+'%','%'+self.query+'%','%'+self.query+'%']
            cursor.execute(sql_select_Query,args)
            records=cursor.fetchall()
            for row in records:
                site=row[0]
                title=row[1]
                break
            if(site=="nope"):
                return "nope"
            if(len(records)>0):
                #print("updating")
                for row in records:
                    c=row[0]+1
                    break
                sql_select_Query = "update shownvideos set count=%s,title=%s where sitelink=%s"
                args=[c,title,site]
                cursor.execute(sql_select_Query,args)
                self.connection.commit()
            else:
                #print("new insert")
                sql_select_Query = "insert into shownvideos(sitelink,count,title) values(%s,%s,%s)"
                recordTuple = (site,1,title)
                cursor.execute(sql_select_Query,recordTuple)
                self.connection.commit()
            return site
#c=connector("service","rto","telangana")
#print(c.getsitelink())

    