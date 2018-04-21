from django.db import models

import uuid

class LoginPin(models.Model):
    key = models.CharField(max_length=6, blank=True, null=True)
    expired = models.BooleanField(default=False)

    def make_key(self): 
        return uuid.uuid4().hex[:6].upper()

    def save(self, *args, **kwargs):
        while True:
            key = self.make_key() 
            if not LoginPin.objects.filter(key=key).exists():
                break
        self.key = key
        super(LoginPin, self).save(*args, **kwargs)

    def __str__(self):
        status = ''
        if self.expired:
            status = 'expired'
        else:
            status = 'active'
        return 'Pin: ' + self.key + ' | Status: ' + status