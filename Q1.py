import math
class Debt:

    def __init__(self, *, debt, interest, repayment, baserepayment):
        self.__debt = debt
        self.__interest = interest
        self.__baseRepayment = baserepayment
        self.__repayment = repayment
        self.__repaid = 0
        self.__repayments = 0

    def __fixtwo(self, float):
        return math.ceil(float*100)/100

    def __calcRepayment(self):
        thisRepayment = self.__fixtwo(self.__debt * self.__repayment)
        thisRepayment = thisRepayment if thisRepayment>self.__baseRepayment else self.__baseRepayment
        thisRepayment = thisRepayment if thisRepayment<= self.__debt else self.__debt
        return thisRepayment

    def __doRepayment(self):
        repayment = self.__calcRepayment()
        self.__debt -= repayment
        self.__repayments += 1
        self.__repaid += repayment
        return (self.__debt>0)

    def __doInterest(self):
        self.__debt += self.__fixtwo(self.__debt * self.__interest)
        return True

    def __doCycle(self):
        self.__doInterest()
        return self.__doRepayment()

    def simulate(self):
        done = False
        while not done:
            done = not self.__doCycle()
        return True

    @property
    def paid(self):
        return "£{:,.2f}".format(self.__repaid)

    @property
    def repayments(self):
        return "{:,}".format(self.__repayments)

    @property
    def interest(self):
        return "{:,.1f}%".format(self.__interest*100)

    @property
    def repayment(self):
        return "{:,.1f}%".format(self.__repayment*100)

    def __str__(self):
        return "{} paid in {} cycle{} at {} interest and {} repayments.".format(
            self.paid,
            self.repayments,
            "s" if self.repayments!=1 else "",
            self.interest,
            self.repayment
        )

def partatest():
    interest = float(input("Interest percentage: "))
    interest = interest/100
    repayment = float(input("Repayment percentage: "))
    repayment = repayment/100
    thisdebt = 100
    baserepayment = 50
    thisdebt = Debt(debt=thisdebt, interest=interest, repayment=repayment, baserepayment=baserepayment)
    thisdebt.simulate()
    return str(thisdebt)

def partbtest():
    interest = 0.43
    repayment = 0.46
    thisdebt = 100
    baserepayment = 50
    thisdebt = Debt(debt=thisdebt, interest=interest, repayment=repayment, baserepayment=baserepayment)
    thisdebt.simulate()
    return str(thisdebt)

def partctest():
    interest = 1
    repayment = 0.51
    thisdebt = 100
    baserepayment = 50
    thisdebt = Debt(debt=thisdebt, interest=interest, repayment=repayment, baserepayment=baserepayment)
    thisdebt.simulate()
    return str(thisdebt)

# 1(a)
#   Demonstrates the program in operation with user inputs.
print("-- 1(a) --\n", partatest())

# 1(b)
#   Simulates debt at 43% interest and 46% repayment
print("\n-- 1(b) --\n", partbtest())

# 1(c)
#   Simulates debt at 100% interest and 51% repayment
#   This is the largest possible interest with the lowest possible repayment rate.
print("\n-- 1(c) --\n", partctest())