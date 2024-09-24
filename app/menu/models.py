from django.db import models

# Create your models here
class Menu(models.Model):
    name = models.CharField()
    url = models.CharField()

    def __str__(self):
        return str(self.name)