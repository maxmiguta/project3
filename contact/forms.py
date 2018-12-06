from django import forms
from django.core.validators import RegexValidator


class ContactForm(forms.Form):
    contact_name = forms.CharField(label='Full name', widget=forms.TextInput({'placeholder': 'Enter your full name'}), required=True)
    contact_email = forms.EmailField(label='Email', widget=forms.TextInput({'placeholder': 'Enter your email'}), required=True)
    phone_number = forms.CharField(validators=[RegexValidator(r'^\d{11}$')], error_messages={'invalid': 'Does not meet requirement'}, required=False, strip=True)
    message = forms.CharField(label='Your enquiry', widget=forms.Textarea({'placeholder': 'Enter your message'}), required=True)