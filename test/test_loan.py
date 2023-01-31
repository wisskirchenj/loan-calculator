import unittest
from creditcalc.loan import Loan


class LoanTest(unittest.TestCase):
    def test_calc_monthly_payment_stage3_ex1(self):
        loan = Loan(1000000, monthly_payment=15000, monthly_interest_rate=10 / 100 / 12)
        self.assertEqual((8, 2), loan.calc_payback_duration())

    def test_calc_monthly_payment_stage3_ex2(self):
        loan = Loan(1000000, payback_duration=60, monthly_interest_rate=10 / 100 / 12)
        self.assertEqual(21248, loan.calc_monthly_payment())

    def test_calc_principal_stage3_ex3(self):
        loan = Loan(monthly_payment=8721.8 , payback_duration=120, monthly_interest_rate=5.6 / 100 / 12)
        self.assertEqual(800000, loan.calc_principal())
