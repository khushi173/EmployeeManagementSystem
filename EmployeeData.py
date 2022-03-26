import sqlite3
con = sqlite3.connect('employee.db')
cur = con.cursor()
sqlite_query = '''CREATE TABLE employee_table(empCode INTEGER PRIMARY KEY ,
                  empName TEXT NOT NULL,
                  empSalary INTEGER NOT NULL,
                  designation TEXT NOT NULL)'''
#cur.execute(sqlite_query)
print('TABLE IS CREATED SUCCESSFULLY')
sqlite_insert_query = '''INSERT INTO employee_table
                         (empCode, empName, empSalary, designation) VALUES
                         (1101, 'Tom', 15000, 'Intern'),
                         (1102, 'John', 28000, 'Junior developer'),
                         (1103, 'Samuel', 45000, 'Senior developer')'''
cur.execute(sqlite_insert_query)
con.commit()
print('Content of the employee table ')
#View All employees
cur.execute(''' SELECT * FROM employee_table ''')
print(cur.fetchall())
con.close()