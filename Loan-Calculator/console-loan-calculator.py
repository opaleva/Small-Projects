from math import ceil, log


def calculate_time(loan_principal: int, payment: float, i: float) -> str:
    years, months = divmod(ceil(log(payment / (payment - i * loan_principal), 1 + i)), 12)
    if months == 0:
        return f"It will take {years} years to repay this loan!"
    elif months == 1:
        return f"It will take 1 month to repay the loan"
    elif years == 0:
        return f"It will take {months} months to repay this loan!"
    elif years == 1:
        return f"It will take 1 year to repay the loan"
    else:
        return f"It will take {years} years and {months} months to repay this loan!"


def calculate_payment(loan_principal: int, periods: int, i: float) -> str:
    return f"Your monthly payment = {ceil(loan_principal * ((i * pow(1 + i, periods)) / (pow(1 + i, periods) - 1)))}!"


def calculate_loan_principal(payment: float, periods: int, i: float) -> str:
    return f"Your loan principal = {round(payment / ((i * pow(1 + i, periods)) / (pow(1 + i, periods) - 1)))}!"


def main():
    options: str = input('What do you want to calculate?\n'
                         'type "n" for number of monthly payments,\n'
                         'type "a" for annuity monthly payment amount,\n'
                         'type "p" for loan principal:\n')

    if options == "n":
        loan_principal: int = int(input("Enter the loan principal:\n"))
        payment: float = float(input("Enter the monthly payment:\n"))
        loan_interest: float = float(input("Enter the loan interest:\n"))
        i: float = loan_interest / 1200
        print(calculate_time(loan_principal, payment, i))
    elif options == "a":
        loan_principal: int = int(input("Enter the loan principal:\n"))
        periods: int = int(input("Enter the number of periods:\n"))
        loan_interest: float = float(input("Enter the loan interest:\n"))
        i: float = loan_interest / 1200
        print(calculate_payment(loan_principal, periods, i))
    elif options == "p":
        payment: float = float(input("Enter the annuity payment:\n"))
        periods: int = int(input("Enter the number of periods:\n"))
        loan_interest: float = float(input("Enter the loan interest:\n"))
        i: float = loan_interest / 1200
        print(calculate_loan_principal(payment, periods, i))


if __name__ == '__main__':
    main()
