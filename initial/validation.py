def validation_number_caractere(self, username): 
    if username == None or len(username) < 5  :
        self._errors['username'] = self.error_class([
            'São requeridos no minimo 6 caracteres'])
