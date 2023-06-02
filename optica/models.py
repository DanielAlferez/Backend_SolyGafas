from django.db import models

# Create your models here.

class OpticaSolyGafas(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    sede = models.CharField(max_length=100)
    nit = models.CharField(max_length=20)

    def __str__(self):
        return self.sede
