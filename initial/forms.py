
from initial.models import Token
from django import forms
from django.contrib.auth.models import User
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


class SignUpPasswordForme(forms.ModelForm):
    password = forms.CharField(max_length=50)
    password_2 = forms.CharField(max_length=50)
    name = forms.CharField(max_length=100)

    
    class Meta:
      model = User
      fields = ['password', 'password_2', 'name']

    