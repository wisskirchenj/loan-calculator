# IDEA EDU Course

Project implemented in the track 'Python for Beginners' of hyperskill.org JetBrains Academy. Purpose of doing this
project is to further practice and stay in touch with Python programming.

## Technology / External Libraries

- Python 3.11.2,
- with packages: argparse, math, io, unittest, unittest.mock

## Repository Contents

The sources of main project tasks (4 stages) and pytest testing.

## Installation

Install the wheel file using pip after clone/fork:

    > pip install dist/loan_calculator-3.11.2-py3-none-any.whl

## Program description

Personal finances are an important part of life. Sometimes you need some extra money and decide to take a loan, or you
want to buy a house using a mortgage. To make an informed decision, you need to be able to calculate different financial
parameters. This program will help us with that!

Have fun!

## Project completion

Project was completed on 02.02.23

## Progress

29.01.23 Project started - gitHub repo and project structure setup.

30.01.23 Stage 1 completed - example print out.

30.01.23 Stage 2 completed - get loan input and calc parameters as rates or duration. Override `__eq__` for test
assertions

31.01.23 Stage 3 completed - annuity payment based loan calculator with monthly interest rate. Diverse calculations
are possible

31.01.23 Final stage 4 completed - calculator now based on argparse of CL-arguments. Besides annuity loans now
differentiated loans are supported, where there is a fixed repayment amount for each monthly payment, thus reducing the
total monthly payments with progressing time. Also, overpayments are calculated to compare different loan types.
