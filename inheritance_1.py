class Car:
  def speed(self):
    print('100km')
class Audi(Car):
  def engine(self):
    print('Engine is powerful')

c = Audi()
c.engine()
c.speed()
