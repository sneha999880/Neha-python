class Employee:
  def set_data(self,n,a,s):
    self.name = n
    self.age = a
    self.salary = s
  def display_data(self):
    print(self.name, self.age , self.salary)

e1  = Employee()
e1.set_data("xxxxx" , 26 , 30000)
e1.display_data()
