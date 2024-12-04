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
c.printCardata()
