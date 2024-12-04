#wap to find the largest even and largest odd in the list

n = int(input())
b=[]
for i in range(n):
  a=int(input())
  b.append(a)

c=[]
d=[]

for i in b:
  if (i%2==0):
    c.append(i)

  else:
    d.append(i)

c.sort()
d.sort()
print("largest even number", c[-1])
print("largest odd number", d[-1])
