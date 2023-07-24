from django.db import models

class movie(models.Model):
    title=models.CharField(max_length=20)
    desc = models.CharField(max_length=20)
    img = models.ImageField(upload_to="travel/img", null=True, blank=True)
