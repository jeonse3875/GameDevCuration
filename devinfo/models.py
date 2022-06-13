from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to="thumbnail",null=True,blank=True)
    
    def __str__(self):
        return self.name

class TagRelation(models.Model):
    parent = models.ForeignKey(Tag,on_delete=models.CASCADE,null=False,related_name='parent_tag')
    child = models.ForeignKey(Tag,on_delete=models.CASCADE,null=False,related_name='child_tag')

    def __str__(self):
        return f'{self.parent} : {self.child}'