from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=64 , blank=False ,unique=True)
    description = models.TextField(default='')
    year = models.PositiveSmallIntegerField(blank=False, default=2000)
    premiere = models.DateField(blank=True, null=True)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2,
                                      null=True, blank=True)
    poster = models.ImageField(upload_to="posters", blank=True,  null=True)

    def title_with_year(self):
        return "{} ({})".format(self.title, self.year)

    def __str__(self):
        return self.title_with_year()