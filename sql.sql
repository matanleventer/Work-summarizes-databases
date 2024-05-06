#Matan Leventer 208447029
---Q5
CREATE TABLE IF NOT EXISTS company
(
company_id INTEGER PRIMARY KEY,
company_name VARCHAR(50) NOT NULL,
company_country VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS ship
(
ship_id INTEGER PRIMARY KEY,
ship_name VARCHAR(50) NOT NULL,
company_id INTEGER,
FOREIGN KEY (company_id) REFERENCES company(company_id) ON UPDATE no action ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS port
(
port_id INTEGER PRIMARY KEY,
port_name VARCHAR(50) NOT NULL,
port_country VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS sail
(
sail_id INTEGER PRIMARY KEY,
port_id_enter INTEGER,
port_id_exit INTEGER,
sail_date date,
ship_id INTEGER,
FOREIGN KEY (port_id_enter) REFERENCES port(port_id) ON UPDATE no action ON DELETE no action,
FOREIGN KEY (port_id_exit) REFERENCES port(port_id) ON UPDATE no action ON DELETE no action,
FOREIGN KEY (ship_id) REFERENCES ship(ship_id) ON UPDATE no action ON DELETE no action,
CONSTRAINT p_id CHECK(port_id_enter != port_id_exit )
);

CREATE TABLE IF NOT EXISTS passenger
(
passenger_id INTEGER PRIMARY KEY,
passenger_firstname VARCHAR(50) NOT NULL,
passenger_lastname VARCHAR(50) NOT NULL,
passenger_birthday date,
passenger_countryborn VARCHAR(50)	
);

CREATE TABLE IF NOT EXISTS employee
(
employee_id INTEGER PRIMARY KEY,
employee_firstname VARCHAR(50) NOT NULL,
employee_lastname VARCHAR(50) NOT NULL,
employee_birthday date,
employee_salary integer,
employee_id_captain INTEGER,
ship_id integer ,
FOREIGN KEY (ship_id) REFERENCES ship(ship_id) ON UPDATE no action ON DELETE no action,
FOREIGN KEY (employee_id_captain) REFERENCES employee(employee_id) ON UPDATE no action ON DELETE no action
);

CREATE TABLE IF NOT EXISTS Ship_Features
(
Ship_id INTEGER PRIMARY KEY,
Ship_width INTEGER,
Ship_length INTEGER,
Ship_occupancy INTEGER,
FOREIGN KEY (ship_id) REFERENCES ship(ship_id) ON UPDATE cascade ON DELETE cascade	
);	

CREATE TABLE IF NOT EXISTS ticket
(
sail_id INTEGER ,
ticket_id INTEGER NOT NULL UNIQUE,
FOREIGN KEY (sail_id) REFERENCES sail(sail_id) ON UPDATE NO ACTION ON DELETE NO ACTION,
CONSTRAINT st_pk PRIMARY KEY(sail_id , ticket_id)
);

CREATE TABLE IF NOT EXISTS buying_tickets_sailing
(
passenger_id INTEGER, 
sail_id INTEGER,
ticket_id INTEGER,
ticket_price INTEGER, 
FOREIGN KEY (sail_id) REFERENCES sail(sail_id) ON UPDATE NO ACTION ON DELETE NO ACTION,
FOREIGN KEY (passenger_id) REFERENCES passenger(passenger_id) ON UPDATE NO ACTION ON DELETE NO ACTION,
FOREIGN KEY (ticket_id) REFERENCES ticket(ticket_id) ON UPDATE NO ACTION ON DELETE NO ACTION,
CONSTRAINT sp_pk PRIMARY KEY(sail_id , passenger_id)
);

CREATE TABLE IF NOT EXISTS Sail_rating
(
sail_id INTEGER ,
passenger_id INTEGER,
Sail_rating INTEGER,
FOREIGN KEY (sail_id) REFERENCES sail(sail_id) ON UPDATE NO ACTION ON DELETE NO ACTION,
FOREIGN KEY (passenger_id) REFERENCES passenger(passenger_id) ON UPDATE NO ACTION ON DELETE NO ACTION,
CONSTRAINT sp_1_pk PRIMARY KEY(sail_id , passenger_id),
CONSTRAINT sr_ch CHECK(Sail_rating >= 1 and  Sail_rating <=5)
);

---Q8
---1
---שלוף את כל תעודות הזהות של הנוסעים ששם הפרטי הוא גיימס שנתנו דירוג מעל ל-2 ומחיר הכרטיס ששילמו גדול מ-3000
select distinct(p.passenger_id)
from passenger as p inner join sail_rating as sr
on p.passenger_id=sr.passenger_id
inner join buying_tickets_sailing as bts
on bts.passenger_id=p.passenger_id
where p.passenger_firstname='James' and sr.sail_rating >2 and bts.ticket_price>3000

---2
---הציגו לכל נוסע את תעודת הזהות שם פרטי ושם משפחה ואת כמות ההפלגות שאליהם יצא
select p.passenger_id,p.passenger_firstname,p.passenger_lastname,count(ticket_id)
from passenger as p left outer join buying_tickets_sailing
on(p.passenger_id = buying_tickets_sailing.passenger_id)
group by p.passenger_id 

---3
---שלוף את תעודות הזהות של כל הנוסעים שלא דירגו אף הפלגה בדירוג 5
select passenger_id
from passenger
EXCEPT
select passenger_id
from sail_rating
where sail_rating=5

---4
---שלוף את כל המדינות שבהם נולדו מעל ל-90 נוסעים משנת 1980
select passenger_countryborn
from passenger
where passenger_birthday >= '1-1-1980'
group by passenger_countryborn
having count(*)>90

---5 
---שלוף את כל מזההי הספינות שיצאו להפלגה מנמל היציאה כמו הפלגה מספר 23904
select distinct(ship_id)
from sail
where port_id_exit=
(select port_id_exit
from sail
where sail_id=23904
)

---6
---הציגו את תעודות הזהות של כל הנוסעים ומחירי הכרטיסים הנמוכים ביותר בכל הפלגה
select passenger_id,ticket_price
from buying_tickets_sailing as bts
where bts.ticket_price =
(select min(bts1.ticket_price)
from buying_tickets_sailing as bts1
where bts.sail_id=bts1.sail_id)

---7
---(1,2,3,4,5)הציגו את תעודות הזהות של כל הנוסעים שדירגו את כל האפשרויות של הציון
select distinct(passenger_id) from
(
select p.passenger_id
from passenger as p join sail_rating as sr
on p.passenger_id = sr.passenger_id
) as sr
where not exists
(
select (sail_rating)
from sail_rating as sr1
where not exists
(	
select (sail_rating)
from sail_rating as sr2
where sr2.passenger_id=sr.passenger_id and sr1.sail_rating=sr2.sail_rating
)
	)

---8
---הציגו את טבלת ההיררכיה של כל העובדים והחזירו את תעודת הזהות,שם פרטי,שם משפחה,תעודת זהות של הקפטן שלהם 
---וטבלת ההיררכיה שלהם כמספר דגרות הניהול מעובד ועד הקטפן הראשי של הספינה שאין מעליו אף אחד ודרגתו 1
with recursive emptable as
(
select captain.employee_id,captain.employee_firstname,captain.employee_lastname,captain.employee_id_captain,1 as emplevel
from employee as captain
where captain.employee_id_captain=captain.employee_id
union all
select emp.employee_id,emp.employee_firstname,emp.employee_lastname,emp.employee_id_captain,emptable.emplevel +1
from employee as emp
join emptable
on emp.employee_id_captain = emptable.employee_id
where emp.employee_id_captain!=emp.employee_id
)
select *
from emptable

---9
---שלוף את כל תאריכים שבאותו היום נולדו בדיוק שלוש הנוסעים ושלוש העובדים 
select passenger_birthday
from passenger
group by passenger_birthday
having count(*)=3
intersect
select employee_birthday
from employee
group by employee_birthday
having count(*)=3


---10
---שלוף את כל תאריכי ההפלגות, שיצאו להפלגה ספינות מחברת הספינות של ישראל ומזהה הספינות שלהם גדול מ1200
select sa.sail_date
from ship as s join company as c
on s.company_id=c.company_id 
join sail as sa 
on s.ship_id=sa.ship_id
where c.company_country ='Israel' and s.ship_id >1200

---Q13
select employee_salary,ship_id,
Lag(employee_salary,5)
over
(partition by ship_id
order by employee_salary) as Prev_employee_salary
from employee

---Q14
select * from (
select e2.employee_salary,e2.ship_id,e1.employee_salary as Prev_employee_salary from(
select employee_id,employee_salary,ship_id, row_number() OVER (PARTITION BY ship_id ORDER BY employee_salary)
from employee) as e1
join (
select employee_id,employee_salary,ship_id, row_number() OVER (PARTITION BY ship_id ORDER BY employee_salary)
from employee) as e2
on e1.ship_id=e2.ship_id and e1.row_number+5=e2.row_number
union all
select employee_salary,ship_id,null as Prev_employee_salary from (
select *, row_number() OVER (PARTITION BY ship_id ORDER BY employee_salary) AS ranka
FROM employee
	) as ma_1
where ma_1.ranka<6
) as n
order by n.ship_id,n.employee_salary, - n.prev_employee_salary desc

---Q15
CREATE OR REPLACE FUNCTION triger() 
   RETURNS TRIGGER 
   LANGUAGE PLPGSQL
AS $$
DECLARE
bonus integer = 1000;

BEGIN
   update employee
   set employee_salary = bonus + employee_salary
   where ship_id = new.ship_id;
   return new;

END;
$$;

CREATE TRIGGER commission BEFORE INSERT ON employee
	for each row EXECUTE FUNCTION triger();
INSERT into employee(
	employee_id,employee_firstname,employee_lastname,employee_birthday,employee_salary,employee_id_captain,ship_id)
	VALUES (208447029,'Matan','Leventer','21-10-1996',500,798654621,1369);