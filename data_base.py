#Matan Leventer 208447029
import psycopg2
from faker import Faker
import random
import pycountry

def connect_to_db(dbname,user,password):
    con = psycopg2.connect(f"dbname={dbname} user={user} password={password}")
    cursor = con.cursor()
    return con,cursor

def populate_db(num_rows,cur):
    e=[]
    for i in range(num_rows):
        id=random.randint(1,300)
        while id in e:
            id = random.randint(1, 300)
        e.append(id)
        country = list_country[id%(len(list_country))]
        name=(country+' shipping company')
        a=(id,name,country)
        cur.execute("INSERT INTO company (company_id,company_name,company_country) values (%s,%s,%s)",(a))


def populate_db(cur):
    cur.execute("select ship_id from ship")
    all = cur.fetchall()
    for i in all:
        num=i
        width=random.randint(50,150)
        length= random.randint(200,400)
        occ=(width//10*length//10)*100+10000
        a=(num,width,length,occ)
        cur.execute("INSERT INTO ship_features (ship_id,ship_width,ship_length,ship_occupancy) values (%s,%s,%s,%s)",(a))

def populate_db(num_rows,cur):
    faker = Faker()
    cur.execute("select distinct(company_country) from company")
    all = cur.fetchall()
    country=[]
    for j in all:
        country.append(j[0])
    e=[]
    for i in range(num_rows):
        id=random.randint(300,400)
        while id in e:
            id = random.randint(300, 400)
        e.append(id)
        name1=faker.email()
        name=name1[:name1.index("@")]
        country= country[id%(len(country))]
        a=(id,name,country)
        cur.execute("INSERT INTO port (port_id,port_name,port_country) values (%s,%s,%s)",(a))


def populate_db(num_rows,cur):
    faker = Faker()
    cur.execute("select company_id from company")
    all = cur.fetchall()
    id_company=[]
    for j in all:
        id_company.append(j[0])
    e=[]
    for i in range(num_rows):
        id=random.randint(1000,1500)
        while id in e:
            id=random.randint(1000,1500)
        e.append(id)
        name1=faker.email()
        name=name1[:name1.index("@")]
        companyid= id_company[id%(len(id_company))]
        a=(id,name,companyid)
        cur.execute("INSERT INTO ship (ship_id,ship_name,company_id) values (%s,%s,%s)",(a))

def populate_db(num_rows,cur):
    faker = Faker()
    e=[]
    for j in range(num_rows):
        sum=0
        for i in range(9):
            random_num = random.randint(0,9)
            sum+=random_num*10**i
        while sum in e:
            sum=0
            for i in range(9):
                random_num = random.randint(0, 9)
                sum += random_num * 10 ** i
        e.append(sum)
        name=faker.first_name()
        last=faker.last_name()
        date=faker.date()
        while (date>'2000' or date<'1930'):
            date = faker.date()
        con=list_country[sum%230]
        a=(sum,name,last,date,con)
        cur.execute("INSERT INTO passenger (passenger_id,passenger_firstname,passenger_lastname,passenger_birthday,passenger_countryborn) values (%s,%s,%s,%s,%s)",(a))

def populate_db(cur):
    z=[]
    cur.execute("select sail_id from sail")
    all = cur.fetchall()
    for i in all:
        z.append(i[0])
    for r in z:
        e=[]
        for j in range(100):
            sum=0
            for i in range(9):
                random_num = random.randint(0,9)
                sum+=random_num*10**i
            if sum in e:
                print('yes')
                while sum in e:
                    sum=0
                    for i in range(8):
                        random_num = random.randint(0, 9)
                        sum += random_num * 10 ** i
            e.append(sum)
            a=(r,sum)
            cur.execute("INSERT INTO ticket (sail_id,ticket_id) values (%s,%s)",(a))

def populate_db(cur):
    passenger=[]
    ticket_sail=[]
    e=[]
    cur.execute("select passenger_id from passenger")
    all = cur.fetchall()
    for i in all:
        passenger.append(i[0])
    cur.execute("select sail_id,ticket_id from ticket")
    all = cur.fetchall()
    for i in all:
        ticket_sail.append((i[0],i[1]))
    for x in range(len(passenger)):
        list1 = []
        if (passenger[x]%3==0):
            number=1
        elif (passenger[x]%5==0):
            number=2
        elif (passenger[x]%8==0):
            number=3
        else:
            number=random.randint(1, 9)
        for j in range(number):
            y=(random.randint(0, 99999))
            while ticket_sail[y][1] in e or ticket_sail[y][0] in list1:
                y = (random.randint(0, 99999))
            list1.append(ticket_sail[y][0])
            e.append(ticket_sail[y][1])
            price = (random.randint(1000, 7500))
            a=(passenger[x],ticket_sail[y][0],ticket_sail[y][1],price)
            cur.execute("INSERT INTO buying_tickets_sailing (passenger_id ,sail_id,ticket_id ,ticket_price) values (%s,%s,%s,%s)",(a))


def populate_db(cur):
    cur.execute("select passenger_id,sail_id from buying_tickets_sailing")
    all = cur.fetchall()
    for i in all:
        number = random.randint(1, 5)
        a=(i[0],i[1],number)
        cur.execute("INSERT INTO sail_rating (passenger_id ,sail_id,sail_rating) values (%s,%s,%s)",(a))

def populate_db(num_rows,cur):
    faker=Faker()
    cur.execute("select ship_id from ship")
    all = cur.fetchall()
    e=[]
    r=[]
    j=[]
    m=[]
    l=[]
    ship=[]
    for i in all:
        ship.append(i[0])
    for iter in range(num_rows):
        sum=0
        for i in range(9):
            random_num = random.randint(0, 9)
            sum += random_num * 10 ** i
        while sum in e:
            sum = 0
            for i in range(9):
                random_num = random.randint(0, 9)
                sum += random_num * 10 ** i
        if iter<len(ship):
            caption=sum
            r.append((sum,ship[iter%200]))
            name=faker.first_name()
            last=faker.last_name()
            date=faker.date()
            while (date>'1990' or date<'1960'):
                date = faker.date()
            saly=salary_1[sum%len(salary_1)]
            a=(sum,name,last,date,saly,caption,ship[iter%200])
            cur.execute("INSERT INTO employee(employee_id,employee_firstname,employee_lastname,employee_birthday,employee_salary,employee_id_captain,ship_id) values (%s,%s,%s,%s,%s,%s,%s)",(a))
        elif iter<800:
            caption=r[iter%200][0]
            j.append((sum,ship[iter%200]))
            name = faker.first_name()
            last = faker.last_name()
            date = faker.date()
            saly = salary_2[sum % len(salary_2)]
            while (date > '1990' or date < '1960'):
                date = faker.date()
            a = (sum, name, last, date, saly, caption, ship[iter % 200])
            cur.execute("INSERT INTO employee(employee_id,employee_firstname,employee_lastname,employee_birthday,employee_salary,employee_id_captain,ship_id) values (%s,%s,%s,%s,%s,%s,%s)",(a))
        elif iter<2400:
            caption=j[iter%600][0]
            m.append((sum,ship[iter%200]))
            name = faker.first_name()
            last = faker.last_name()
            date = faker.date()
            while (date > '1990' or date < '1960'):
                date = faker.date()
            saly = salary_3[sum % len(salary_3)]
            a = (sum, name, last, date, saly, caption, ship[iter % 200])
            cur.execute("INSERT INTO employee(employee_id,employee_firstname,employee_lastname,employee_birthday,employee_salary,employee_id_captain,ship_id) values (%s,%s,%s,%s,%s,%s,%s)",(a))
        elif iter<9600:
            caption=m[iter%1600][0]
            l.append((sum,ship[iter%200]))
            name = faker.first_name()
            last = faker.last_name()
            date = faker.date()
            while (date > '1990' or date < '1960'):
                date = faker.date()
            saly = salary_4[sum % len(salary_4)]
            a = (sum, name, last, date, saly, caption, ship[iter % 200])
            cur.execute("INSERT INTO employee(employee_id,employee_firstname,employee_lastname,employee_birthday,employee_salary,employee_id_captain,ship_id) values (%s,%s,%s,%s,%s,%s,%s)",(a))
        else:
            caption = l[iter % 200][0]
            name = faker.first_name()
            last = faker.last_name()
            date = faker.date()
            while (date > '1990' or date < '1960'):
                date = faker.date()
            saly = salary_5[sum % len(salary_5)]
            a = (sum, name, last, date, saly, caption, ship[iter % 200])
            cur.execute("INSERT INTO employee(employee_id,employee_firstname,employee_lastname,employee_birthday,employee_salary,employee_id_captain,ship_id) values (%s,%s,%s,%s,%s,%s,%s)",(a))


def populate_db(num_rows,cur):
    faker = Faker()
    cur.execute("select port_id from port")
    all = cur.fetchall()
    e=[]
    r=[]
    z=[]
    for i in all:
        e.append(i[0])
    cur.execute("select ship_id from ship")
    all = cur.fetchall()
    for i in all:
        z.append(i[0])
    for x in range(num_rows):
        random_num=random.randint(10000,99999)
        random_num_1 = random.randint(10000, 99999)
        while random_num%50 ==random_num_1%50 or random_num in r:
            random_num = random.randint(10000,99999)
            random_num_1 = random.randint(10000, 99999)
        r.append(random_num)
        port_id_enter=e[random_num%50]
        port_id_exist=e[random_num_1 % 50]
        ship_id=z[random_num%200]
        date=faker.date()
        while (date<'2010'):
            date = faker.date()
        a=(random_num,port_id_enter,port_id_exist,date,ship_id)
        cur.execute("INSERT INTO sail (sail_id,port_id_enter,port_id_exit,sail_date,ship_id) values (%s,%s,%s,%s,%s)",(a))


def close_communication(cur,conn):
    cur.close()
    conn.close()

def get_countries():
    list=[]
    for x in pycountry.countries:
        list.append(x.name)
    return list


def delete_all_rows(cur):
    cur.execute("delete from sail_rating")

list_country=get_countries() # list of countries
num_rows=10000 # number or rows i want to enter
salary_1=[25000,30000,50000,45000,35000,20000,55000,22500,37500,47500,32500,27500,22150] # salary captain
salary_2=[16000,16500,17000,17500,18000,18500,19000,19500] # salary
salary_3=[13500,12000,11000,10000,10500,15000,13000,12500,11500] # salary
salary_4=[4500,3000,3500,6500,8000,9000,8500,9500,7000,4000,6000,6500,5500,7500,8500] # salary
salary_5=[500,750,1000,1250,1500,1750,2000] # salary

