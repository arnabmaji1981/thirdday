class student():
    def _int_(self, rollno, name):
        self.rollno = rollno
        self.name = name

    def displaystudent(self):
        print("rollno:", self.rollno, "name:", self.name)

emp1 = student(121, "ajeet")
emp2 = student(122, "sonu")
emp1.displaystudent()
emp2.displaystudent()
