import argparse
from argparse import ArgumentParser

from creditcalc.loan import Loan


def get_duration_info(loan: Loan):
    def pluralized_or_empty(unit: str, amount: int) -> str:
        if amount == 0:
            return ''
        if amount == 1:
            return f'1 {unit} '
        return f'{amount} {unit}s '

    years, months = loan.payback_duration // 12, loan.payback_duration % 12
    return (f'It will take {pluralized_or_empty("year", years)}' + ('and ' if years > 0 else '')
            + f'{pluralized_or_empty("month", months)}to repay this loan!')


def get_loan_info(loan: Loan) -> str:
    match loan.mode:
        case "duration":
            return get_duration_info(loan)
        case "monthly":
            return f'Your annuity payment = {loan.monthly_payment}!'
        case "principal":
            return f'Your loan principal = {loan.principal}!'
        case "diff":
            return '\n'.join([f'Month {i + 1}: payment is {payment}'
                              for i, payment in enumerate(loan.diff_payments)])


def args_are_valid(args: argparse.Namespace) -> bool:
    interest_valid = args.interest and args.interest > 0
    periods_valid_if_given = not args.periods or args.periods > 0
    principal_valid_if_given = not args.principal or args.principal > 0
    payment_valid_if_given = not args.payment or args.payment > 0
    parameter_count_valid = len(list(filter(None, args.__dict__.values()))) == 4
    type_valid_with_options = args.type == 'diff' and not args.payment or args.type == 'annuity'
    return (interest_valid
            and periods_valid_if_given
            and principal_valid_if_given
            and payment_valid_if_given
            and parameter_count_valid
            and type_valid_with_options)


def parse_commandline_arguments() -> argparse.Namespace | None:
    parser = ArgumentParser(description='Loan calculator app')
    parser.add_argument('--type', help='Type of payment - use annuity or diff = differentiated')
    parser.add_argument('--interest', help='Annual interest rate in %', type=float)
    parser.add_argument('--principal', help='Loan principal', type=float)
    parser.add_argument('--payment', help='Monthly payment (only if type = "annuity")', type=float)
    parser.add_argument('--periods', help='Number of payback months', type=int)
    args = parser.parse_args()
    return args if args_are_valid(args) else None


def main():
    args = parse_commandline_arguments()
    if not args:
        print('Incorrect parameters')
        return
    loan = Loan(**args.__dict__)
    print(get_loan_info(loan))
    print('Overpayment =', int(loan.get_overpayment()))


if __name__ == '__main__':
    main()
