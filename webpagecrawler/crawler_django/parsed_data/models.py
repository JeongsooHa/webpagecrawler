from django.db import models

# Create your models here.
class SDsaramData(models.Model):
    title = models.CharField(max_length=200)
    #link = models.URLField()

    #Change normal title to data title
    def __str__(self):
        return self.title

