from django.db import models

class Reviews(models.Model):

    review = models.CharField(max_length=70)
    playerId = models.ForeignKey("Player",on_delete=models.CASCADE)
    gamesId =models.ForeignKey("Games",on_delete=models.CASCADE)