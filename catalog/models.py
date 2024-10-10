from django.db import models

class Author(models.Model):
    surname = models.CharField(max_length=30, unique=True) 

class Book(models.Model):
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE,)
    year = models.CharField(max_length=4)