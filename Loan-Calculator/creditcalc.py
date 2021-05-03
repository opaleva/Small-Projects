from math import ceil, log
from argparse import ArgumentParser, Namespace


def calculate_diff(i: float, args: Namespace) -> str:
    overpayment = 0
    for m in range(1, args.periods + 1):
        month = ceil((args.principal / args.periods) + i * (
                args.principal - ((args.principal * (m - 1)) / args.periods)))
        overpayment += month
        print(f'Month {m}: payment is {month}')
    print()
    return f'Overpayment = {ceil(overpayment - args.principal)}'


def calculate_time(i: float, args: Namespace) -> str:
    years, months = divmod(ceil(log(args.payment / (args.payment - i * args.principal), 1 + i)), 12)
    overpayment = ceil((years * 12 + months) * args.payment - args.principal)
    if months == 0:
        return f"It will take {years} years to repay this loan!\nOverpayment = {overpayment}"
    elif months == 1:
        return f"It will take 1 month to repay the loan!\nOverpayment = {overpayment}"
    elif years == 0:
        return f"It will take {months} months to repay this loan!\nOverpayment = {overpayment}"
    elif years == 1:
        return f"It will take 1 year to repay the loan!\nOverpayment = {overpayment}"
    elif years > 1 and months > 1:
        return f"It will take {years} years and {months} months to repay this loan!\nOverpayment = {overpayment}"



def calculate_payment(i: float, args: Namespace) -> str:
    annuity_payment = ceil(args.principal * ((i * pow(1 + i, args.periods)) / (pow(1 + i, args.periods) - 1)))
    overpayment = abs(int(args.principal - annuity_payment * args.periods))
    return f"Your annuity payment = {annuity_payment}!\n" \
           f"Overpayment = {overpayment}"


def calculate_loan_principal(i: float, args: Namespace) -> str:
    loan_principal = round(args.payment / ((i * pow(1 + i, args.periods)) / (pow(1 + i, args.periods) - 1)))
    overpayment = ceil(args.periods * args.payment - loan_principal)
    return f"Your loan principal = {loan_principal}!\n" \
           f"Overpayment = {overpayment}"


def main():
    parser: ArgumentParser = ArgumentParser(description="This program will help you make loan calculations.")
    parser.add_argument('--type', '--first_parameter', choices=['annuity', 'diff'],
                        help='Type of loan calculation: --annuity for individual values or --diff for calculation of '
                             'differentiated payment')
    parser.add_argument('--principal', '--second_parameter', type=float, help="loan principal")
    parser.add_argument('--payment', '--third_parameter', type=float, help="monthly payment amount")
    parser.add_argument('--periods', '--fourth_parameter', type=int, help="number of months")
    parser.add_argument('--interest', '--fifth_parameter', type=float, help="loan percentage")
    args: Namespace = parser.parse_args()

    options: list = [args.type, args.principal, args.payment, args.periods, args.interest]
    if (args.type != 'diff' and args.type != 'annuity') or (args.type == 'diff' and args.payment) or \
            not args.interest or len(options) < 4:
        print('Incorrect parameters')

    if args.type == 'diff' and args.interest:
        i: float = args.interest / 1200
        print(calculate_diff(i, args))

    elif args.type == 'annuity':
        if args.principal and args.payment and args.interest:
            i = args.interest / 1200
            print(calculate_time(i, args))
        elif args.periods and args.principal:
            i = args.interest / 1200
            print(calculate_payment(i, args))
        elif args.payment and args.periods:
            i = args.interest / 1200
            print(calculate_loan_principal(i, args))


if __name__ == '__main__':
    main()
