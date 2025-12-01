from django.db import models
from django.contrib.auth.models import  User
from django.db.models.signals import post_save
from django.dispatch import receiver
from sorl.thumbnail import ImageField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        related_name = "profile"
    )
    image_profile = ImageField(upload_to='profiles/images/', blank=True, null=True)

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender = User)
def created_user_profile(sender, instance, created, **kwargs):
    if (created):
        Profile.objects.create(user = instance)