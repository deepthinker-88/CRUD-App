
from django.db import models



# Create your models here.
class Grandparent(models.Model):
    first_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=30,null=True)
    age = models.SmallIntegerField(null=True)
    daughter_name = models.ManyToManyField('parent.Parent',related_name='daughter',blank=True)
    son_name = models.ManyToManyField('parent.Parent',related_name = 'son',blank=True)
    grandchildren = models.ManyToManyField('cousin.Cousin',blank=True,related_name = 'grandchild')
    

    class Meta:
        verbose_name_plural= "Taylor/Lindsay Grandparents"

    # delete age filed, create new field called date of bith 
    # create method that calculates age and display age in the view 
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
