from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=240, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True) # nullable
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title[0:100]