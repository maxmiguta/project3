from django import forms
#from phonenumber_field.formfields import PhoneNumberField


class ContactForm(forms.Form):
    contact_name = forms.CharField(label='Enter your name', required=True)
    contact_email = forms.EmailField(label='Enter your email', required=True)
	#phone_number = PhoneNumberField(label='Enter your phone number')
    message = forms.CharField(label='Enter your message', widget=forms.Textarea, required=True)