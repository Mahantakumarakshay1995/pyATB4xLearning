#custom exception

class less_money_exception(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(message)

balance =100
withdrow = int(input("Enter the amount you want withdraw"))

if withdrow > balance:
    raise less_money_exception("Balance is Low!")
else:
    print("Remain Bal", (balance-withdrow))