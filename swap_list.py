#imp : swapping is important and all its type
#with var without var....
#wap to swap the first and last value of the list

size = int(input())
list1 = list(map(int,input().split()))
list1[0] = list1[0] + list1[-1]
list1[-1] = list1[0] - list1[-1]
list1[0] = list1[0] -list1[-1]

list1
