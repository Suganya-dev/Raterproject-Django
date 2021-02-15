from django.db import models

class Games(models.Model):

    rater=models.ForeignKey("Rater", on_delete=models.CASCADE)
    title= models.CharField(max_length=50)
    description= models.CharField(max_length=30)
    designer= models.CharField(max_length=30)
    Number_of_players = models.IntegerField()
    releaseYear= models.IntegerField()
    timeToPlay= models.IntegerField()
    ageRec= models.IntegerField()
