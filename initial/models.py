from django.db import models
from django.utils import timezone

import datetime

class Token(models.Model):
    token = models.CharField(max_length=64)
    publishing_date = models.DateTimeField(default=timezone.now, blank=True,)


    
    @property
    def delete_after_five_minutes(self):
        time = self.publishing_date + datetime.timedelta(minutes=2)
        if self.publishing_date < datetime.datetime.now()-datetime.timedelta(minutes=1):
            e = Token.objects.get(pk=self.pk)
            e.delete()
            return True
        else:
            return False