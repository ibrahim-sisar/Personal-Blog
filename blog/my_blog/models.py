from django.db import models
# Create your models here.
class Blog(models.Model):
    name=models.CharField(max_length=500)
    body=models.TextField()
    creatd=models.DateField(auto_now_add=True)


