def divisible_by_2_and_4():
    for num in range(2, 51):
        if num % 2 == 0 and num % 4 == 0:
            yield num
for num in divisible_by_2_and_4():
    print(num)
