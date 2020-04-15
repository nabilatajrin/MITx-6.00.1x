balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


for i in range(12):
    balance = balance - (balance * monthlyPaymentRate)
    + ((balance - (balance * monthlyPaymentRate)) * (annualInterestRate/12))

print(('remaining balance:', balance))
print(('remaining balance:', round(balance, 2)))