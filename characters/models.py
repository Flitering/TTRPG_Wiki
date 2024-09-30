from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=100)
    race = models.CharField(max_length=50)
    character_class = models.CharField(max_length=50)
    level = models.IntegerField(default=1)
    attributes = models.JSONField(default=dict)

    def __str__(self):
        return self.name
