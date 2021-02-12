from django.db import models

class Category(models.Model):

    label=models.CharField(max_length=25)
    playerId = models.ForeignKey("Player",on_delete=models.CASCADE)