class Car:
  'Common_car'
  car=0
  def __init__(self,name,id):
    self.name=name
    self.id=id
    Car.car+=1

  def printCardata(self):
    print("Name: " ,self.name , "id:" ,self.id)

c = Car("Audi" , 2000000)
c1 = Car("Benz" , 3000000)
c2 = Car("BMW" , 10000000)

c.printCardata()
c1.printCardata()
c2.printCardata()
