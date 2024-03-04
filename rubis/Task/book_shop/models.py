from django.db import models
from .constants import RATINGS


class book(models.Model):
    title = models.CharField(max_length=50, blank=False)
    author = models.CharField(max_length=50, blank=False)
    publication = models.CharField(max_length=50, blank=False)
    year = models.CharField(max_length=50,blank=False)

    class Meta:
        db_table = 'book'

class review(models.Model):
    book_review = models.TextField(max_length=500, blank=False)
    rating = models.IntegerField( choices=RATINGS ,blank=False)
    book = models.ForeignKey(book, on_delete=models.CASCADE, blank=False)

    class Meta:
        db_table = 'review'





