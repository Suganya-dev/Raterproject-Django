from django.db import models

class Ratings(models.Model):

    rating = models.IntegerField
    playerId = models.ForeignKey("Player",on_delete=models.CASCADE)
    gamesId = models.ForeignKey("Games",on_delete=models.CASCADE)