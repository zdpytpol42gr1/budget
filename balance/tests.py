from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase

from balance.models import Expense, Income

User = get_user_model()


class ExpenseTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="test01", email="a@a.pl", password="niewiem")

    def test_is_decimal(self):
        expense = Expense.objects.create(expense_name="test", expense_value=91.01,
                                         recurring_expense=True, user=self.user)
        self.assertIsInstance(expense.expense_value, Decimal, 'Wrong type of expense value')

    def test_decimal_validator(self):
        expense = Expense.objects.create(expense_name="test", expense_value=Decimal('-91.91').quantize(Decimal('1.00')),
                                         recurring_expense=True, user=self.user)
        self.assertGreaterEqual(expense.expense_value, Decimal('0.01').quantize(Decimal('1.00')),
                                'can create value lower than validator says')

    def test_blank_expense_name(self):
        expense = Expense.objects.create(expense_name="", expense_value=Decimal('150.09').quantize(Decimal('1.00')),
                                         recurring_expense=True, user=self.user)
        self.assertIsNot(expense.expense_name, '', 'Name can\'t be empty string')


class IncomeTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="test01", email="a@a.pl", password="niewiem")

    def test_is_decimal(self):
        income = Income.objects.create(income_name="test", income_value=91.01,
                                         recurring_income=True, user=self.user)
        self.assertIsInstance(income.income_value, Decimal, 'Wrong type of income value')

    def test_decimal_validator(self):
        income = Income.objects.create(income_name="test", income_value=Decimal('-91.91').quantize(Decimal('1.00')),
                                         recurring_income=True, user=self.user)
        self.assertGreaterEqual(income.income_value, Decimal('0.01').quantize(Decimal('1.00')),
                                'can create value lower than validator says')

    def test_blank_income_name(self):
        income = Income.objects.create(income_name="", income_value=Decimal('130.09').quantize(Decimal('1.00')),
                                         recurring_income=True, user=self.user)
        self.assertIsNot(income.income_name, '', 'Name can\'t be empty string')

