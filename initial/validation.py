from django.contrib.auth.models import User
from .models import PreUser

"""Valida o user name e email"""
def validation_number_caractere(self, username): 
    if username == None or len(username) < 5  :
        self._errors['username'] = self.error_class([
            'São requeridos no minimo 6 caracteres em username'])


def user_exists_pre(self, username):
    pre = PreUser.objects.all()
    for p in pre:
        if username in p.username:
            self._errors['username'] = self.error_class([
                'Nome de usuário já está sendo ultilizado'])

def user_exists(self, username):
    user = User.objects.all()
    for u in user:
        if username in u.username:
            self._errors['username'] = self.error_class([
                'Nome de usuário já está sendo ultilizado'])

def the_email_field_cannot_be_blank(self, email):
    if email == None:
        self._errors['email'] = self.error_class([
            'O campo email é obrigatorio'])

def validation_email_equal(self, email, email_2):
    if email != email_2:
        self._errors['email'] = self.error_class([
            'Os Campos email e confirmmação de email tende ser iguais'])


def Checking_existing_email(self, email):
    try:
        query = PreUser.objects.get(email=email)
    except PreUser.DoesNotExist:
        query = None

    if query != None:
        self._errors['email'] = self.error_class([
            'Este email já está sendo ultilizado'])     


"""Valida compo de senha"""

def password_equal(self, password, password_2):
    if password != password_2:
        self._errors['email'] = self.error_class([
            'Os Campos de senha estão diferentes'])

def size_password(self, password, password_2):
    if len(password) <= 6 or len(password) >= 50:
        self._errors['email'] = self.error_class([
                    'Senhas tem que ser mior que 6 carqacteres e menor que 50 caracteres'])
