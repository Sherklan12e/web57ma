# usuario/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=Profile.user)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    print(f"Signal triggered for User: {instance}")
    if created:
        Profile.objects.create(user=instance)
        print('a')
    else:
        instance.profile.save()
        print("hola")
