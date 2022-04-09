from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    score = models.DecimalField(decimal_places=3, max_digits=10)

    def __str__(self):
        return self.id+self.name+self.score