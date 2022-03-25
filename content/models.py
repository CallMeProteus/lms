from django.db import models

# Create your models here.
class Content(models.Model):
    title  =  models.CharField(max_length=200,)
    description  =  models.TextField(blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    def __str__(self) -> str:
            if self.year:
                return f"{self.title} ({self.year})"

            return self.title