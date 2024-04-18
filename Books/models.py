from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Book(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    # date_created = models.DateTimeField(auto_now_add=True,auto_now=True)
    price = models.DecimalField(max_digits=20,decimal_places=2)
    author = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='cover/',blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail',args=[self.id])

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(get_user_model(),on_delete = models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='comments')
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

