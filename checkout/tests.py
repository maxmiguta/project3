from django.test import TestCase
from .forms import OrderForm
from django import forms


class CustomOrderTest(TestCase):

    # Test to check that validation works when a user doesn't provide their full name
    def test_order_form_fails_with_missing_full_name(self):
        order_form = OrderForm({
            'phone_number': '01234567890',
            'street_address1': 'address',
            'town_or_city': 'city',
            'postcode': 'ab1 2cd',
            'country': 'country',
        })
        self.assertFalse(order_form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your name",
                                 order_form.full_clean())

    # Test to check that validation works when a user doesn't provide their phone number
    def test_order_form_fails_with_missing_phone_number(self):
        order_form = OrderForm({
            'full_name': 'full name',
            'street_address1': 'address',
            'town_or_city': 'city',
            'postcode': 'ab1 2cd',
            'country': 'country',
        })
        self.assertFalse(order_form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your phone number",
                                 order_form.full_clean())

    # Test to check that validation works when a user doesn't provide their address
    def test_order_form_fails_with_missing_address(self):
        order_form = OrderForm({
            'full_name': 'full name',
            'phone_number': '01234567890',
            'town_or_city': 'city',
            'postcode': 'ab1 2cd',
            'country': 'country',
        })
        self.assertFalse(order_form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your address",
                                 order_form.full_clean())