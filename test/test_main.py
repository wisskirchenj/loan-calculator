import unittest
import sys
from creditcalc.loan import Loan
from creditcalc.main import get_loan_info, parse_commandline_arguments


class MainTest(unittest.TestCase):

    def test_get_loan_info_stage3_ex1(self):
        loan = Loan(type='annuity', principal=1000000, payment=15000, interest=10)
        self.assertEqual('It will take 8 years and 2 months to repay this loan!', get_loan_info(loan))

    def test_get_loan_info_stage3_ex2(self):
        loan = Loan(type='annuity', principal=1000000, periods=60, interest=10)
        self.assertEqual('Your annuity payment = 21248!', get_loan_info(loan))

    def test_get_loan_info_stage3_ex3(self):
        loan = Loan(type='annuity', payment=8721.8, periods=120, interest=5.6)
        self.assertEqual('Your loan principal = 800000!', get_loan_info(loan))

    def test_prompt_for_loan_stage4_ex1(self):
        sys.argv = ['prog', '--type=diff', '--principal=1000000', '--periods=10', '--interest=10']
        args = parse_commandline_arguments()
        self.assertEqual('diff', args.type)
        self.assertEqual(1000000.0, args.principal)
        self.assertIsNone(args.payment)
        self.assertEqual(10, args.interest)
        self.assertEqual(10, args.periods)
        loan = Loan(**args.__dict__)
        self.assertEqual('''Month 1: payment is 108334
Month 2: payment is 107500
Month 3: payment is 106667
Month 4: payment is 105834
Month 5: payment is 105000
Month 6: payment is 104167
Month 7: payment is 103334
Month 8: payment is 102500
Month 9: payment is 101667
Month 10: payment is 100834''', get_loan_info(loan))
        self.assertEqual(45837, loan.get_overpayment())

    def test_prompt_for_loan_stage4_ex2(self):
        sys.argv = ['prog', '--type=annuity', '--principal=1000000', '--periods=60', '--interest=10']
        args = parse_commandline_arguments()
        self.assertEqual('annuity', args.type)
        self.assertEqual(1000000.0, args.principal)
        self.assertIsNone(args.payment)
        self.assertEqual(10, args.interest)
        self.assertEqual(60, args.periods)
        loan = Loan(**args.__dict__)
        self.assertEqual('Your annuity payment = 21248!', get_loan_info(loan))
        self.assertEqual(274880, loan.get_overpayment())

    def test_prompt_for_loan_stage4_ex3(self):
        sys.argv = ['prog', '--type=diff', '--principal=1000000', '--payment=10400']
        args = parse_commandline_arguments()
        self.assertIsNone(args)

    def test_prompt_for_loan_stage4_ex4(self):
        sys.argv = ['prog', '--type=diff', '--principal=500000', '--periods=8', '--interest=7.8']
        args = parse_commandline_arguments()
        self.assertEqual('diff', args.type)
        self.assertEqual(500000.0, args.principal)
        self.assertIsNone(args.payment)
        self.assertEqual(7.8, args.interest)
        self.assertEqual(8, args.periods)
        loan = Loan(**args.__dict__)
        self.assertEqual('''Month 1: payment is 65750
Month 2: payment is 65344
Month 3: payment is 64938
Month 4: payment is 64532
Month 5: payment is 64125
Month 6: payment is 63719
Month 7: payment is 63313
Month 8: payment is 62907''', get_loan_info(loan))
        self.assertEqual(14628, loan.get_overpayment())

    def test_prompt_for_loan_stage4_ex5(self):
        sys.argv = ['prog', '--type=annuity', '--periods=120', '--payment=8722', '--interest=5.6']
        args = parse_commandline_arguments()
        self.assertEqual('annuity', args.type)
        self.assertIsNone(args.principal)
        self.assertEqual(8722.0, args.payment)
        self.assertEqual(5.6, args.interest)
        self.assertEqual(120, args.periods)
        loan = Loan(**args.__dict__)
        self.assertEqual('Your loan principal = 800018!', get_loan_info(loan))
        self.assertEqual(246622, loan.get_overpayment())

    def test_prompt_for_loan_stage4_ex6(self):
        sys.argv = ['prog', '--type=annuity', '--principal=500000', '--payment=23000', '--interest=7.8']
        args = parse_commandline_arguments()
        self.assertEqual('annuity', args.type)
        self.assertEqual(500000.0, args.principal)
        self.assertEqual(23000.0, args.payment)
        self.assertEqual(7.8, args.interest)
        self.assertIsNone(args.periods)
        loan = Loan(**args.__dict__)
        self.assertEqual('It will take 2 years and to repay this loan!', get_loan_info(loan))
        self.assertEqual(52000, loan.get_overpayment())