class Student:
    def _init(self, name):
        print("This is a paremeterized constructor")
        self.name=name
    def show(self):
        print("Hello", self.name)
student = Student( "arnab" )
student.show()

