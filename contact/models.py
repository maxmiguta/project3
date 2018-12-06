from django.db import models
from django.core.validators import RegexValidator


class ContactForm(models.Model):
    phone_regex = RegexValidator(regex=r'^\d{11}$', message="Phone number must have 11 digits.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)