from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth import get_user_model
# Create your models here.


class Authar(models.Model):
    name= models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, help_text='the book title')
    tags = TaggableManager()
    published_date = models.DateTimeField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnail/', null=True, blank=True)
    poster = models.ImageField(upload_to='image/', null=True, blank=True)
    no_of_reads = models.IntegerField(default=0)
    authars = models.ManyToManyField(Authar,related_name="books", null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    long_description = models.TextField(null=True, blank=True)
    isbn = models.CharField(max_length=20, null=True, blank=True)
    page_count = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, default='Publish')
    def __str__(self):
        return self.title


class Reader(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    no_of_reading_books = models.IntegerField(default=0)
    books = models.ManyToManyField(Book, related_name='book_readers')