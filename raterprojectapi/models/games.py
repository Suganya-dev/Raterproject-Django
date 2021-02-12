from django.db import models

class Player(models.Model):

    title= models.CharField(max_length=50)
    description= models.CharField(max_length=30)
    designer= models.CharField(max_length=30)
    releaseYear= models.IntegerField()
    timeToPlay= models.CharField(max_length=20)
    ageRec= models.IntegerField()
    categoryId= models.ForeignKey("Category",on_delete=models.CASCADE)