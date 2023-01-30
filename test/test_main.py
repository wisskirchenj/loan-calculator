import unittest
from unittest.mock import patch
from creditcalc.loan import Loan
from creditcalc.main import get_loan_info, prompt_for_loan


class MainTest(unittest.TestCase):
    def test_get_loan_info_stage2_ex1(self):
        loan = Loan(1000, monthly_payment=150)
        self.assertEqual('It will take 7 months to repay the loan', get_loan_info(loan, 'm'))

    def test_get_loan_info_stage2_ex2(self):
        loan = Loan(1000, monthly_payment=1000)
        self.assertEqual('It will take 1 month to repay the loan', get_loan_info(loan, 'm'))

    def test_get_loan_info_stage2_ex3(self):
        loan = Loan(1000, payback_duration=10)
        self.assertEqual('Your monthly payment = 100', get_loan_info(loan, 'p'))

    def test_get_loan_info_stage2_ex4(self):
        loan = Loan(1000, payback_duration=9)
        self.assertEqual('Your monthly payment = 112 and the last payment = 104', get_loan_info(loan, 'p'))

    @patch('builtins.input')
    def test_prompt_for_loan_stage2_ex1(self, mock_input):
        mock_input.side_effect = ['1000', 'm', '150']
        loan = Loan(1000, monthly_payment=150)
        self.assertEqual((loan, 'm'), prompt_for_loan())

    @patch('builtins.input')
    def test_prompt_for_loan_stage2_ex2(self, mock_input):
        mock_input.side_effect = ['1000', 'm', '1000']
        loan = Loan(1000, monthly_payment=1000)
        self.assertEqual((loan, 'm'), prompt_for_loan())

    @patch('builtins.input')
    def test_prompt_for_loan_stage2_ex3(self, mock_input):
        mock_input.side_effect = ['1000', 'p', '10']
        loan = Loan(1000, payback_duration=10)
        self.assertEqual((loan, 'p'), prompt_for_loan())

    @patch('builtins.input')
    def test_prompt_for_loan_stage2_ex4(self, mock_input):
        mock_input.side_effect = ['1000', 'p', '9']
        loan = Loan(1000, payback_duration=9)
        self.assertEqual((loan, 'p'), prompt_for_loan())
