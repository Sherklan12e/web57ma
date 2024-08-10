from django.contrib import admin
from .models import Profile, Intereses,Rating,Comment

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'pais')

@admin.register(Intereses)
class InterestAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
admin.site.register(Rating)
admin.site.register(Comment)