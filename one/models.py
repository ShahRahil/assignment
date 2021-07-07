from django.db import models
#rahil , rahil@email.com , socialmedia
# Create your models here.
class newpost(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, null=False, blank=False, default="abc@xyz.com")
    location = models.CharField(max_length=20, default="India")
    description = models.TextField()
    image = models.ImageField(null=False,blank=False)
    def __str__(self):
        return self.name

class comment(models.Model):
    content = models.CharField(max_length=500)
    def __str__(self):
        return self.content