#wap to find the how many digits in the given number

x = int(input())

z = str(x)
tot_digit = 0
for i in z:
  tot_digit += 1

print(tot_digit)
