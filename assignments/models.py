from django.db import models


# Create your models here.
class Assignments(models.Model):
    title  =  models.CharField(max_length=200,)
    description  =  models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title