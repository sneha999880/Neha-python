#print the first n natural numbers starts from 1 to n

n = int(input())
for i in range(1,n+1):
  print(i,end=" ")

#while loop

n = int(input())
i = 1 #initialisation 
while i<=n: #condition
  print(i,end=" ")
  i += 1 #increment

#factorial
n = int(input())
fact = 1
for i in range(1,n+1):
  fact = fact * i
print(fact ,end=" ")

#wap to find no.of characters and digits in a string

#hint: 
#for <var> in <sequence>:
#      <body stmts>
#       isdigit()
#       isalpha()

x = input()
digit = 0
alpha = 0
for i in x:
  if i.isdigit():
    digit += 1
  elif i.isalpha():
    alpha += 1
print("digit = " , digit)
print("letter = ", alpha)
