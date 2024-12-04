class Calculator:
  def add(self,num1,num2):
    self.num1=num1
    self.num2=num2
    return self.num1+self.num2
  def sub(self,num1,num2):
    return num1-num2

class AdvancedCalculator(Calculator):
  def mul(self,num1,num2):
    print('Multiplication: ' ,num1*num2)
  def div(self,num1,num2):
    return num1//num2

x = AdvancedCalculator()
num1 = int(input())
num2 = int(input())
print('addition:%d'(x.add(num1,num2)))
print('subtraction:' ,x.sub(num1,num2))
x.mul(num1,num2)
print("floor division: %d"%(x.div(num1,num2)))
