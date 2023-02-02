import unittest
from creditcalc.loan import Loan


class LoanTest(unittest.TestCase):
    def test_calc_monthly_payment_stage3_ex1(self):
        loan = Loan(principal=1000000, payment=15000, interest=10, type='annuity')
        self.assertEqual(98, loan.calc_payback_duration())

    def test_calc_monthly_payment_stage3_ex2(self):
        loan = Loan(principal=1000000, type='annuity', periods=60, interest=10)
        self.assertEqual(21248, loan.calc_monthly_payment())

    def test_calc_principal_stage3_ex3(self):
        loan = Loan(type='annuity', payment=8721.8 , periods=120, interest=5.6)
        self.assertEqual(800000, loan.calc_principal())
