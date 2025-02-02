from django.db import models

class AddedInfo(models.Model):
    TYPES = {
        (0, 'Other'),
        (1, 'Horror'),
        (2, 'Comedy'),
        (3, 'Sci-Fi'),
        (4, 'Drama'),
    }

    duration = models.PositiveSmallIntegerField(default=0)
    type = models.PositiveSmallIntegerField(default=0,  choices=TYPES)

class Video(models.Model):
    title = models.CharField(max_length=64 , blank=False ,unique=True)
    description = models.TextField(default='')
    year = models.PositiveSmallIntegerField(blank=False, default=2000)
    premiere = models.DateField(blank=True, null=True)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2,
                                      null=True, blank=True)
    poster = models.ImageField(upload_to="posters", blank=True,  null=True)

    added = models.OneToOneField(AddedInfo, on_delete=models.CASCADE, null=True, blank=True)

    def title_with_year(self):
        return "{} ({})".format(self.title, self.year)

    def __str__(self):
        return self.title_with_year()


class Review(models.Model):
    review = models.TextField(default='', blank=True)
    stars = models.PositiveSmallIntegerField(default=0)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

class Actor(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    vides = models.ManyToManyField(Video, related_name='actors')