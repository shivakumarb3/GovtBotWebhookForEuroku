import mysql.connector
connection = mysql.connector.connect(host='database-1.chlducbyghdc.us-east-2.rds.amazonaws.com',
                                         database='Governmentbotdb',
                                         user='admin',password='shiva123')
sql_select_Query = "select * from shownvideos"
cursor=connection.cursor()
cursor.execute(sql_select_Query)
records=cursor.fetchall()
for row in records:
    print(row[0])
    print(row[1])
    print(row[2])
    print("......")
    