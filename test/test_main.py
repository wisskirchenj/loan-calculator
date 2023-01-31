import unittest
from unittest.mock import patch
from creditcalc.loan import Loan
from creditcalc.main import get_loan_info, prompt_for_loan


class MainTest(unittest.TestCase):

    def test_get_loan_info_stage3_ex1(self):
        loan = Loan(1000000, monthly_payment=15000, monthly_interest_rate=10 / 12 / 100)
        self.assertEqual('It will take 8 years and 2 months to repay this loan!', get_loan_info(loan, 'n'))

    def test_get_loan_info_stage3_ex2(self):
        loan = Loan(1000000, payback_duration=60, monthly_interest_rate=10 / 12 / 100)
        self.assertEqual('Your monthly payment = 21248!', get_loan_info(loan, 'a'))

    def test_get_loan_info_stage3_ex3(self):
        loan = Loan(monthly_payment=8721.8, payback_duration=120, monthly_interest_rate=5.6 / 12 / 100)
        self.assertEqual('Your loan principal = 800000!', get_loan_info(loan, 'p'))

    @patch('builtins.input')
    def test_prompt_for_loan_stage3_ex1(self, mock_input):
        mock_input.side_effect = ['n', '1000000', '15000', '10']
        loan = Loan(1000000, monthly_payment=15000, monthly_interest_rate=10 / 12 / 100)
        self.assertEqual((loan, 'n'), prompt_for_loan())

    @patch('builtins.input')
    def test_prompt_for_loan_stage3_ex2(self, mock_input):
        mock_input.side_effect = ['a', '1000000', '60', '10']
        loan = Loan(1000000, payback_duration=60, monthly_interest_rate=10 / 12 / 100)
        self.assertEqual((loan, 'a'), prompt_for_loan())

    @patch('builtins.input')
    def test_prompt_for_loan_stage2_ex3(self, mock_input):
        mock_input.side_effect = ['p', '8721.8', '120', '5.6']
        loan = Loan(monthly_payment=8721.8, payback_duration=120, monthly_interest_rate=5.6 / 12 / 100)
        self.assertEqual((loan, 'p'), prompt_for_loan())

