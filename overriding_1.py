class Animal:
  def sound(self):
    print("Some generic sound")

class Dog(Animal):
  def sound(self):
    print('bark')
class Cat(Animal):
  def sound(self):
    print('meow')

dog = Dog() #creating instance of class
cat = Cat() #creating instance of class

#overriding
#taking output from child classes not parent class
dog.sound()
cat.sound()
