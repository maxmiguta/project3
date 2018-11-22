from django import forms
from phonenumber_field.formfields import PhoneNumberField


class ContactForm(forms.Form):
    contact_name = forms.CharField(label='Full name', widget=forms.TextInput({'placeholder': 'Enter your full name'}), required=True)
    contact_email = forms.EmailField(label='Email', widget=forms.TextInput({'placeholder': 'Enter your email'}), required=True)
    phone_number = PhoneNumberField(label='Phone number', widget=forms.TextInput({'placeholder': 'Enter your number'}))
    message = forms.CharField(label='Your enquiry', widget=forms.Textarea({'placeholder': 'Enter your message'}), required=True)