from django.db import models

# Create your models here.
class Tambola2(models.Model):
        str1=models.CharField(max_length=128)
        random_number=models.PositiveIntegerField()

        def __str__(self):
                return str(self.str1)

