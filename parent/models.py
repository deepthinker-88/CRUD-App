from django.db import models
from grandparent.models import Grandparent
# from cousin.models import Cousin


# Create your models here.
class Parent(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mother_name = models.ForeignKey(
        Grandparent,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="mother_name",
    )
    father_name = models.ForeignKey(
        Grandparent,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="father_name",
    )

    son_name = models.ManyToManyField("cousin.Cousin")
    daughter_name = models.ManyToManyField(
        "cousin.Cousin", related_name="daughter", blank=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "Lindsay/Taylor Parents"
