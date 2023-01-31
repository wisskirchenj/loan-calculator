from creditcalc.loan import Loan

PRINCIPAL_QUESTION = 'Enter the loan principal:\n'
MODE_QUESTION = '''What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:\n'''
PAYMENT_QUESTION = 'Enter the monthly payment:\n'
DURATION_QUESTION = 'Enter the number of periods:\n'
INTEREST_QUESTION = 'Enter the loan interest:\n'


def prompt_for_loan() -> tuple[Loan, str]:
    mode = input(MODE_QUESTION)
    loan_dict = dict()
    if mode != "p":
        loan_dict['principal'] = float(input(PRINCIPAL_QUESTION))
    if mode != "a":
        loan_dict['monthly_payment'] = float(input(PAYMENT_QUESTION))
    if mode != "n":
        loan_dict['payback_duration'] = float(input(DURATION_QUESTION))
    loan_dict['monthly_interest_rate'] = float(input(INTEREST_QUESTION)) / 100 / 12
    return Loan(**loan_dict), mode


def get_loan_info(loan: Loan, mode: str) -> str:
    if mode == "n":
        years, months = loan.calc_payback_duration()
        return (f'It will take {years} years and {months} month{"" if months == 1 else "s"}'
                + ' to repay this loan!')
    elif mode == "a":
        return f'Your monthly payment = {loan.calc_monthly_payment()}!'
    else:
        return f'Your loan principal = {loan.calc_principal()}!'


def main():
    loan, mode = prompt_for_loan()
    print(get_loan_info(loan, mode))


if __name__ == '__main__':
    main()
