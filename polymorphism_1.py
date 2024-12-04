class RBI:
    def interest(self):
        return "Rate of Interest from RBI not specified"

class SBI(RBI):
    def interest(self):
        return 2.3

class IndianBank(RBI):
    def interest(self):
        return 2.4

class Canara(RBI):
    def interest(self):
        return 2.7
sbi = SBI()
indian_bank = IndianBank()
canara = Canara()
print(f"SBI Rate of Interest: {sbi.interest()}%")
print(f"Indian Bank Rate of Interest: {indian_bank.interest()}%")
print(f"Canara Rate of Interest: {canara.interest()}%")
