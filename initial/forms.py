from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import fields

class RegisterForme(forms.ModelForm):
    model = User
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get("email")        
        if email == '':
            raise ValidationError("O campo email não pode ficar vazio")
        else:
            return email
        
    class Meta:
        model = User
        fields = ['username', 'email']