from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=300, blank=True)
    about = models.TextField()
    url = models.URLField()
    image = CloudinaryField('image')

    def __str__(self):
        return self.title

class Contact(models.Model):
    email = models.CharField(max_length=300)
    subject = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.email