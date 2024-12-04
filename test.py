class test:
  def __init__(self):
    self.variable = 'Car'
    self.Change(self.variable)
  def Change(self,var):
    var = 'Bike'
obj = test()
print(obj.variable)
