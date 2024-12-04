class Animal:
  def sound(self):
    print("Some generic sound")

class dog(Animal):
  def sound(self):
    print("dog barks")
d=dog()
d.sound()
class cat(Animal):
  def sound(self):
    print("cat meows")
c=cat()
c.sound()
