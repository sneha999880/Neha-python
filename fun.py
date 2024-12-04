#declaring different variables outside the functions 

def sum(n1,n2):
  s = n1+n2
  return s
x = int(input("enter value 1: "))
y = int(input("enter value 2: "))
sum(x,y)

#without return type
def fun():
  print("welcome to python")
fun()

#lambda function
sum = lambda x,y : x+y
sum(1,2)
 
