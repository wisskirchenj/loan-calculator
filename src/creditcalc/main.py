from creditcalc.loan import Loan

PRINCIPAL_QUESTION = 'Enter the loan principal:\n'
MODE_QUESTION = '''What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:\n'''
PAYMENT_QUESTION = 'Enter the monthly payment:\n'
DURATION_QUESTION = 'Enter the number of months:\n'


def prompt_for_loan() -> tuple[Loan, str]:
    principal = float(input(PRINCIPAL_QUESTION))
    mode = input(MODE_QUESTION)
    if mode == "m":
        return Loan(principal, monthly_payment=float(input(PAYMENT_QUESTION))), mode
    else:
        return Loan(principal, payback_duration=int(input(DURATION_QUESTION))), mode


def get_loan_info(loan: Loan, mode: str) -> str:
    if mode == "m":
        return (f'It will take {loan.calc_payback_duration()} month{"" if loan.calc_payback_duration() == 1 else "s"}'
                + ' to repay the loan')
    else:
        monthly, last = loan.calc_monthly_payment()
        return f'Your monthly payment = {monthly}' + (f' and the last payment = {last}' if monthly != last else '')


def main():
    loan, mode = prompt_for_loan()
    print(get_loan_info(loan, mode))


if __name__ == '__main__':
    main()
