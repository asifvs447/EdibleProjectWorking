from django.contrib import admin
from .models import LoginPin

class LoginPinAdmin(admin.ModelAdmin):
    readonly_fields = ('key', 'expired')


admin.site.register(LoginPin, LoginPinAdmin)