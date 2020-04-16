balance = 5000.00
annualInterestRate = 0.02

monthlyPaymentRate = 0
init_balance = balance
monthlyInterestRate = annualInterestRate/12

# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

while balance > 0:
    for i in range(12):
        balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)

    if balance > 0:
        monthlyPaymentRate += 10
        balance = init_balance
    elif balance <= 0:
        break

print('Lowest payment:', monthlyPaymentRate)