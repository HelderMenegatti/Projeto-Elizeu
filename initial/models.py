from django.db import models

class PreUser(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    email_2 = models.EmailField()
    token = models.CharField(max_length=50)