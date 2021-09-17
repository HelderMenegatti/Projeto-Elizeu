from django.db import models

class Token(models.Model):
    id_user = models.IntegerField()
    token = models.CharField(max_length=50)