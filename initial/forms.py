from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.forms import fields
from initial.validation import *

class RegisterForme(forms.ModelForm):
    model = User
    email = forms.EmailField()

        
    class Meta:
        model = User
        fields = ['username', 'email']

    
    def clean(self):
        super(RegisterForme, self).clean()
        username = self.cleaned_data.get('username')       
        email = self.cleaned_data.get("email")  

        validation_number_caractere(self, username)

        # elif username in User.objects.all():
        #     self._errors['username'] = self.error_class([
        #         'Nome de usuário já existe'])
        return self.cleaned_data