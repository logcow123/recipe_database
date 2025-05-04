import sqlite3
from employee import Employee

# creates a context manager
# you can use the name of a file to save it or ":memory:" to use RAM which will not save
conn = sqlite3.connect(':memory:')

# creates a cursor that can run sqlite code
c = conn.cursor()

c.execute("""CREATE TABLE employees (
             first text,
             last text,
             pay integer
          )""")

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {"first": emp.first, "last": emp.last, "pay": emp.pay})

def get_emps_by_name(lname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lname})
    return c.fetchall()

def update_emp_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay=:pay
                     WHERE first=:first AND last=:last""",
                     {'pay': pay, 'first' : emp.first, 'last': emp.last})
        
def delete_emp(emp):
    with conn:
        c.execute("""DELETE FROM employees WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last})

emp1 = Employee('John', 'Doe', 5000)
emp2 = Employee('Mark', 'Grayson', 70000)
emp3 = Employee('Nolan', 'Grayson', 20000)

insert_emp(emp1)
insert_emp(emp2)
insert_emp(emp3)

print(get_emps_by_name('Grayson'))
print(get_emps_by_name('Doe'))

print()

update_emp_pay(emp2, 10000000)
delete_emp(emp3)

print(get_emps_by_name('Grayson'))
#Creates the table

# Ways to Insert
# c.execute("INSERT INTO employees VALUES ('Walter', 'White', 650)")

# Uses '?' and a tuple
# c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp1.first, emp1.last, emp2.pay))

# Uses a :variable_name and a dictionary
# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {"first": emp2.first, "last": emp2.last, "pay": emp2.pay})

#commits the current transaction
#conn.commit()

#closes the connection
conn.close()