import sqlite3
from employee import Employee

conn = sqlite3.connect('employee.db')

c = conn.cursor()

# create employees table
# c.execute("""CREATE TABLE EMPLOYEES (
#             first text,
#             last text,
#             pay integer
#             )""")

# c.execute("INSERT INTO EMPLOYEES values ('Vinay','Jain',50000)")

# c.execute("INSERT INTO EMPLOYEES values ('Aarti','Jain',70000)")

# c.execute("select * from employees where first = 'Aarti'")

# print "-"
# print (c.fetchone())
# print (c.fetchall())
# print "-"
# print (c.fetchone())    # alrady fetched all records
# print "-"
# print (c.fetchone())
#
# conn.commit()
# conn.close()

emp_1 = Employee('John','Doe',80000)
emp_2 = Employee('Jane','Doe',90000)

print (emp_1.first)
print (emp_1.last)
print (emp_1.pay)

# /Users/Anvi/PycharmProjects