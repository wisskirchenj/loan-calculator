import math


class Loan:
    def __init__(self, principal: float, monthly_payment: float = None, payback_duration: int = None):
        self.principal = principal
        self.monthly_payment = monthly_payment
        self.payback_duration = payback_duration

    def __eq__(self, other):
        return (type(other) == Loan
                and self.principal == other.principal
                and self.monthly_payment == other.monthly_payment
                and self.payback_duration == other.payback_duration)

    def calc_payback_duration(self) -> int:
        """Calculate the payback duration in months using principal and monthly_payment properties"""
        return math.ceil(self.principal / self.monthly_payment)

    def calc_monthly_payment(self) -> tuple[int, int]:
        """
        Calculate the monthly payment using principal and payback_duration properties
        :return: tuple of monthly payment and last payment (which may differ)
        """
        monthly_payment = math.ceil(self.principal / self.payback_duration)
        last_payment = int(self.principal - (self.payback_duration - 1) * monthly_payment)
        return monthly_payment, last_payment
