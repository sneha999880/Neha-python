# use while loop to sum of n and average numbers

n = int(input("Enter the value of n: "))
sum = 0
i = 1
while i <= n:
  sum += i
  i += 1
print(sum)
print(sum/n)
