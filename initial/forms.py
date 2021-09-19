from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.forms import fields
from initial.validation import *

class RegisterForme(forms.ModelForm):
    model = User
    email = forms.EmailField()
    email_two = forms.EmailField()

        
    class Meta:
        model = User
        fields = ['username', 'email', 'email_two']

    
    def clean(self):
        super(RegisterForme, self).clean()
        username = self.cleaned_data.get('username')       
        email = self.cleaned_data.get("email")
        email_two = self.cleaned_data.get("email_two")  

        validation_number_caractere(self, username)
        
        user_exists(self, username)

        the_email_field_cannot_be_blank(self, email)

        validation_email_equal(self, email, email_two)

        Checking_existing_email(self, email)

        return self.cleaned_data