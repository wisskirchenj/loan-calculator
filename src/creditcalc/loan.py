import math


class Loan:
    def __init__(self, principal: float = None, monthly_payment: float = None,
                 payback_duration: int = None, monthly_interest_rate: float = 0):
        self.principal = principal
        self.monthly_payment = monthly_payment
        self.payback_duration = payback_duration
        self.monthly_interest_rate = monthly_interest_rate

    def __eq__(self, other):
        return (type(other) == Loan
                and self.principal == other.principal
                and self.monthly_payment == other.monthly_payment
                and self.payback_duration == other.payback_duration
                and self.monthly_interest_rate == other.monthly_interest_rate)

    def calc_payback_duration(self) -> (int, int):
        """Calculate the payback duration in years and months using loan properties"""
        months = math.log(self.monthly_payment /
                          (self.monthly_payment - self.monthly_interest_rate * self.principal),
                          1 + self.monthly_interest_rate)
        months = math.ceil(months)
        return months // 12, months % 12

    def calc_monthly_payment(self) -> int:
        """Calculate the monthly payment using loan properties"""
        return math.ceil(self.principal * self.calc_annuity_factor())

    def calc_principal(self) -> int:
        """Calculate the principal using loan properties"""
        return math.floor(self.monthly_payment / self.calc_annuity_factor())

    def calc_annuity_factor(self) -> float:
        interest_factor = math.pow(1 + self.monthly_interest_rate, self.payback_duration)
        return self.monthly_interest_rate * interest_factor / (interest_factor - 1)
