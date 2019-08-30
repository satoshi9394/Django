#user admin classes

#django
from django.contrib import admin

#models
from users.models import Profile

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    #Profile admin
    list_display = ('user','phone_number','website','picture')