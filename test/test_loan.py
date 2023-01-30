import unittest
from creditcalc.loan import Loan


class LoanTest(unittest.TestCase):
    def test_calc_payback_duration_stage2_ex1(self):
        loan = Loan(1000, monthly_payment=150)
        self.assertEqual(7, loan.calc_payback_duration())

    def test_calc_payback_duration_stage2_ex2(self):
        loan = Loan(1000, monthly_payment=1000)
        self.assertEqual(1, loan.calc_payback_duration())

    def test_calc_monthly_payment_stage2_ex3(self):
        loan = Loan(1000, payback_duration=10)
        self.assertEqual((100, 100), loan.calc_monthly_payment())

    def test_calc_monthly_payment_stage2_ex4(self):
        loan = Loan(1000, payback_duration=9)
        self.assertEqual((112, 104), loan.calc_monthly_payment())
