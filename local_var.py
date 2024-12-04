#write a code to differentiate local and global var - ques in exam
total = 0
def sum (arg1, arg2):
  total = arg1 + arg2 #total is inside function - local
  print("Inside the function local total:", total)
  return total
sum(10,20)
print("Outside the function global total:", total)
