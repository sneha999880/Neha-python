class Car:
  'Common_car'
  car=0
  def __init__(self,name,id):
     self.name=name
     self.id=id
     Car.car+=1
  def printCardata(self):
       print("Name:",self.name,"Id:",self.id)
c=Car("AUDI",2000000)
c1=Car("BENZ",3000000)
c2=Car("BMW",1000000)
print("Total Cars:",Car.car)
c.printCardata()
c1.printCardata()
c2.printCardata()
