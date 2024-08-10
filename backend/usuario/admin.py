from django.contrib import admin
from .models import Profile, Intereses

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'pais')

@admin.register(Intereses)
class InterestAdmin(admin.ModelAdmin):
    list_display = ('nombre',)