from django.db import models
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=240, blank=False, null=False)
    image = ImageField(upload_to='feed/images/', blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True) # nullable
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 

    def __str__(self):
        return self.title[0:100]