from django.db import models


class BookList(models.Model):
    author_first_name = models.CharField(max_length=30)
    author_last_name = models.CharField(max_length=30)
    book_title = models.CharField(max_length=60)
    list_pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.book_title
