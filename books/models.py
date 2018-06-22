from django.db import models

# Create your models here.


class Media(models.Model):
    original_title = models.CharField(max_length=1000, unique=True)
    volume = models.CharField(max_length=200)
    authors = models.CharField(max_length=500)
    publication_date = models.DateTimeField()
    publisher = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    ISBN_13 = models.CharField(max_length=30)
    read = models.CharField(max_length=10)
    storage = models.CharField(max_length=30)
    book_info = models.CharField(max_length=500)
    category = models.CharField(max_length=50)
    rental = models.CharField(max_length=30)
    comment = models.CharField(null=True, max_length=1000)

    def __str__(self):
        return self.observation_ID
