#wap to remove the duplicate items from the code

size_of_list = int(input())
list_1 = list(map(int,input().split()))
b = []
unique = []
for x in list_1:
  if x not in b:
    unique.append(x)
    b.append(x)
print("Non-duplicate items:")
print(unique)
