from django.db import models

class Movies(models.Model):
    name = models.CharField(max_length=100)
    rating = models.FloatField()


    def __str__(self):
        return str(self.name) 