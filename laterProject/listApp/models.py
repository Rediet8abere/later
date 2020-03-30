from django.db import models
from django.utils import timezone
from django.urls import reverse


class Books(models.Model):
    # author_name = models.CharField(max_length=30)
    # author_last_name = models.CharField(max_length=30)
    book_title_or_author_name = models.CharField(max_length=100, default='what do you wanna read')
    list_pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.book_title_or_author_name

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk':self.pk})
