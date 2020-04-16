balance = 5000.00
annualInterestRate = 0.02
monthlyPaymentRate = 0.04


# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)


for i in range(1):
    balance = balance - ((balance - monthlyPaymentRate)
    + (balance - (balance * monthlyPaymentRate)) * (annualInterestRate/12))

print(('remaining balance:', balance))
print(('remaining balance:', round(balance, 2)))