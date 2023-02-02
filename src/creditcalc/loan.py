import math


class Loan:
    def __init__(self, type: str, principal: float = None, payment: float = None,
                 periods: int = None, interest: float = 0):
        self.type = type
        self.principal = principal
        self.monthly_payment = payment
        self.payback_duration = periods
        self.monthly_interest_rate = interest / 100 / 12
        self.diff_payments = []
        self.mode = self.get_mode()
        self.calc_missing()

    def __eq__(self, other):
        return (type(other) == Loan
                and self.type == other.type
                and self.principal == other.principal
                and self.monthly_payment == other.monthly_payment
                and self.payback_duration == other.payback_duration
                and self.monthly_interest_rate == other.monthly_interest_rate)

    def calc_payback_duration(self) -> int:
        """Calculate the payback duration in years and months using loan properties"""
        months = math.log(self.monthly_payment /
                          (self.monthly_payment - self.monthly_interest_rate * self.principal),
                          1 + self.monthly_interest_rate)
        return math.ceil(months)

    def calc_monthly_payment(self) -> int:
        """Calculate the monthly payment using loan properties"""
        return math.ceil(self.principal * self.calc_annuity_factor())

    def calc_principal(self) -> int:
        """Calculate the principal using loan properties"""
        return math.floor(self.monthly_payment / self.calc_annuity_factor())

    def calc_annuity_factor(self) -> float:
        interest_factor = math.pow(1 + self.monthly_interest_rate, self.payback_duration)
        return self.monthly_interest_rate * interest_factor / (interest_factor - 1)

    def calc_differentiated_payment(self, i) -> int:
        return math.ceil((1 + self.monthly_interest_rate * (self.payback_duration - i))
                         * self.principal / self.payback_duration)

    def calc_diff_payments(self) -> list[int]:
        return [self.calc_differentiated_payment(i) for i in range(self.payback_duration)]

    def get_mode(self) -> str:
        return 'diff' if self.type == 'diff' else self.get_annuity_mode()

    def get_annuity_mode(self):
        if not self.principal:
            return 'principal'
        elif not self.payback_duration:
            return 'duration'
        return 'monthly'

    def calc_missing(self):
        match self.mode:
            case 'diff':
                self.diff_payments = self.calc_diff_payments()
            case 'principal':
                self.principal = self.calc_principal()
            case 'duration':
                self.payback_duration = self.calc_payback_duration()
            case 'monthly':
                self.monthly_payment = self.calc_monthly_payment()

    def get_overpayment(self) -> float:
        if self.mode == 'diff':
            return sum(self.diff_payments) - self.principal
        else:
            return self.payback_duration * self.monthly_payment - self.principal
