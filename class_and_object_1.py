class NumberCheck:
    def __init__(self, number):
        self.number = number

    def check_sign(self):
        if self.number > 0:
            return "Positive"
        elif self.number < 0:
            return "Negative"
        else:
            return "Zero"

num = NumberCheck(26)
print(f"The number is {num.check_sign()}.")
