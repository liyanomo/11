import unittest
from student import *
from datetime import datetime, date



class TestStudent(unittest.TestCase):



    def setUp(self):
        conn.init("test_students.db")
        Student.create_table()
        Course.create_table()
        Student_Course.create_table()

    def tearDown(self):
        Student.drop_table()
        Course.drop_table()
        Student_Course.drop_table()          


    def test_add_student(self):
        student = add_student("Max", "Adams", 24, "Spb")
        cursor = conn.cursor() 
        cursor.execute(f'''select * from student where id={student.id} ''')
        st = cursor.fetchone()
        self.assertEqual(st[1], "Max")
        self.assertEqual(st[2], "Adams")
        self.assertEqual(int(st[3]), 24)
        self.assertEqual(st[4], "Spb")

    def test_add_course(self):
        course = add_course("python", date(2021, 7, 21), date(2021, 12, 21))
        cursor = conn.cursor()  
        cursor.execute(f'''select * from course where id={course.id} ''')
        st = cursor.fetchone() 
        self.assertEqual(st[1], course.name)
        start = datetime.strptime(st[2], '%Y-%m-%d')
        end = datetime.strptime(st[3], '%Y-%m-%d')
        self.assertEqual(date(start.year, start.month, start.day), course.time_start)
        self.assertEqual(date(end.year, end.month, end.day), course.time_end)

    def test_delete_student(self):
        student = add_student("Max", "Adams", 24, "Spb")
        course = add_course("python", date(2021, 7, 21), date(2021, 12, 21))
        sc = add_student_course(student.id, course.id)
        delete_student(sc.id,student.id)

        cursor = conn.cursor()  
        cursor.execute(f'''select * from student where id={student.id} ''')
        st = cursor.fetchone()
        self.assertIsNone(st)
        cursor.execute(f'''select * from student_course where id={sc.id} ''')
        sc_sql = cursor.fetchone()
        self.assertIsNone(sc_sql)

    def test_add_student_course(self):
        student = add_student("Max", "Adams", 24, "Spb")
        course = add_course("python", date(2021, 7, 21), date(2021, 12, 21))
        sc = add_student_course(student.id,course.id)
        cursor = conn.cursor()
        cursor.execute(f'''select * from student_course where id={sc.id} ''')
        st = cursor.fetchone()
        self.assertEqual(st[1],student.id)
        self.assertEqual(st[2],course.id)
       

if __name__ == "__main__":
    unittest.main()
