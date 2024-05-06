#Matan Leventer 208447029
import psycopg2
from faker import Faker

def connect_to_db(dbname,user,password):
    con = psycopg2.connect(f"dbname={dbname} user={user} password={password}")
    cursor = con.cursor()
    return con,cursor

def populate_db(cur):
    faker = Faker()
    cur.execute("select distinct(s1.sail_date),s1.sail_id from sail as s1 join sail as s2 on s1.sail_date=s2.sail_date and s1.sail_id!=s2.sail_id")
    date_1=cur.fetchall()
    cur.execute("select distinct(sail_date) from sail")
    all_1 = cur.fetchall()
    list_date=set(all_1)
    for i in range(len(date_1)):
        new_date = faker.date()
        while (new_date in list_date or new_date<'2010'):
            new_date = faker.date()
        list_date.add(new_date)
        sail_id_1=date_1[i][1]
        a=(new_date,sail_id_1)
        cur.execute("update sail set sail_date = (%s) where sail_id =(%s) ",(a[0],a[1]))

def close_communication(cur,conn):
    cur.close()
    conn.close()

conn,cur =connect_to_db("test_database","tester","test_password")
populate_db(cur)
conn.commit()
close_communication(cur,conn)