from django.db import models
from django.utils import timezone
from django.urls import reverse


class Books(models.Model):
    author_name = models.CharField(max_length=30)
    # author_last_name = models.CharField(max_length=30)
    book_title = models.CharField(max_length=60)
    list_pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.book_title

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk':self.pk})
