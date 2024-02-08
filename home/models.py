from django.db import models

# Create your models here.
# this is home models 
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=13)
    content = models.TextField()




