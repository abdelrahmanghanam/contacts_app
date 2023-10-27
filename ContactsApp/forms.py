from django import forms
from ContactsApp.models import Contact,PhoneNumber


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["first_name", "last_name", "email"]


class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ["country_code", "phone_number", "contact_id"]