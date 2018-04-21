from django.db import models

# Create your models here.

class LoginPin(models.Model):
    otp = models.CharField(max_length=6, blank=False)
    expired = models.BooleanField(default=False)