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