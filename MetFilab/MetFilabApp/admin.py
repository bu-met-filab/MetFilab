from django.contrib import admin

# Register your models here.
from MetFilabApp.models.app import profile

admin.site.register(profile.Profile)