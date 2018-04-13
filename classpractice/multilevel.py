class Animal:
    def eat(self):
        print("Eating")
class Dog(Animal):
    def bark(self):
        print("barking")
class BabyDog(Dog):
    def weef(self):
        print("weeping")
d=BabyDog()
d.eat()
d.bark()
d.weef()
'''
class Animal:   
    def eat(self):  
      print 'Eating...'  
class Dog(Animal):  
   def bark(self):  
      print 'Barking...'  
class BabyDog(Dog):  
    def weep(self):  
        print 'Weeping...'  
d=BabyDog()  
d.eat()  
d.bark()  
d.weep()  '''
