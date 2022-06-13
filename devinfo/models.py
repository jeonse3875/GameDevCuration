from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to="thumbnail",null=True,blank=True)
    tags = models.ManyToManyField('Tag')
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to="thumbnail",null=True,blank=True)
    children = models.ManyToManyField('Tag', blank=True)
    
    def __str__(self):
        return self.name