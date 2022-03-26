import unittest
import sqlite3

class employees(unittest.TestCase):
    def setUp(self):
        self.connection=sqlite3.connect("employee.db")
        self.empCode= "1102"
        self.empName= "John"

    def tearDown(self):
        self.empCode="0"
        self.empCode= ""
        self.connection.close()

    def test_case1(self):
        result = self.connection.execute("SELECT empName FROM employee_table where empCode ="+self.empCode)
        for i in result:
            fetchname =i[0]
        self.assertEqual(fetchname,self.empName)




if __name__=="__main__":
    unittest.main()