
from initial.models import PreUser
from django import forms
from django.contrib.auth.models import User
from initial.validation import *



class PreUserForme(forms.ModelForm):
    
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    email_2 = forms.EmailField()


        
    class Meta:
        model = PreUser
        fields = ['username', 'email', 'email_2']

    
    def clean(self):
        super(PreUserForme, self).clean()
        username = self.cleaned_data.get('username')       
        email = self.cleaned_data.get("email")
        email_2 = self.cleaned_data.get("email_2")  

        validation_number_caractere(self, username)
        
        user_exists(self, username)

        user_exists_pre(self, username)

        the_email_field_cannot_be_blank(self, email)

        validation_email_equal(self, email, email_2)

        Checking_existing_email(self, email)

        return self.cleaned_data


class SignUpPasswordForme(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_2 = forms.CharField(widget=forms.PasswordInput())


    
    class Meta:
      model = User
      fields = ['password', 'password_2']

    def clean(self):
        super(SignUpPasswordForme, self).clean()

        password = self.cleaned_data.get('password')
        password_2 = self.cleaned_data.get('password_2')

        password_equal(self, password, password_2)
        
        size_password(self, password, password_2)


class loginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    