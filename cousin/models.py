from django.db import models

#from parent.models import Parent
from grandparent.models import Grandparent
from parent.models import Parent


# Create your models here.

class Cousin(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.SmallIntegerField(null=True)
    #grandfather = models.ForeignKey(Grandparent,on_delete=models.CASCADE,related_name='grandfathers',null=True,blank=True)
    #grandmother = models.ForeignKey(Grandparent,on_delete=models.CASCADE,related_name ='grandmothers',null=True,blank=True)
    grandfathers = models.ManyToManyField('grandparent.grandparent',blank=True,related_name='Grandfathers')
    grandmothers= models.ManyToManyField('grandparent.grandparent',blank=True,related_name='Grandmothers')
    father = models.ForeignKey(Parent,on_delete=models.CASCADE,related_name='father',null=True,blank=True)
    mother = models.ForeignKey(Parent,on_delete=models.CASCADE,related_name='mother',null=True,blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "Cousin Info/Sister_Info"
 