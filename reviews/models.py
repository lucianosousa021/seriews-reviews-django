from django.db import models

# Create your models here.
class SeriesReviews(models.Model):
    serie_name = models.CharField(max_length=50)
    serie_genre = models.CharField(max_length=50)
    serie_rating = models.IntegerField()
    serie_info = models.TextField()
    serie_note = models.TextField()

    def __str__(self):
        return self.serie_name
