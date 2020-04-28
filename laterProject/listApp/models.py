from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

class Books(models.Model):
    # author_name = models.CharField(max_length=30)
    # author_last_name = models.CharField(max_length=30)
    book_title = models.CharField(max_length=100, default='What do you want to read?')
    author_name = models.CharField(max_length=100, default='Who inspires you?')
    image = models.CharField(max_length=200, default='http://placehold.it/700x400')
    description = models.TextField()
    list_pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.book_title_or_author_name

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk':self.pk})

class Musics(models.Model):
    # author_name = models.CharField(max_length=30)
    # author_last_name = models.CharField(max_length=30)
    artist = models.CharField(max_length=100, default='What would you like to hear?')
    list_pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.artist

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk':self.pk})
