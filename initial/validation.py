from django.contrib.auth.models import User

def validation_number_caractere(self, username): 
    if username == None or len(username) < 5  :
        self._errors['username'] = self.error_class([
            'São requeridos no minimo 6 caracteres em username'])


def user_exists(self, username):
    if username in User.objects.all():
        self._errors['username'] = self.error_class([
            'Nome de usuário já existe'])

def the_email_field_cannot_be_blank(self, email):
    if email == None:
        self._errors['email'] = self.error_class([
            'O campo email é obrigatorio'])

def validation_email_equal(self, email, email_two):
    if email != email_two:
        self._errors['email'] = self.error_class([
            'Os Campos email e confirmmação de email tende ser iguais'])


def Checking_existing_email(self, email):
    try:
        query = User.objects.get(email=email)
    except User.DoesNotExist:
        query = None

    if query != None:
        self._errors['email'] = self.error_class([
            'Este email já está sendo ultilizado'])     
