from django.db import models

# Create your models here.
class Food(models.Model):
    title = models.CharField(max_length=100)
    photo_url = models.TextField(max_length=500)
    benefits = models.TextField(max_length=5000)

    def __str__(self):
        return self.title

class Quotes(models.Model):
    quote = models.TextField(max_length=5000)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.quote

class Meditate(models.Model):
    title = models.CharField(max_length=100)
    moderator = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    preview_url = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100, default='')
    message = models.TextField(max_length=5000, default='')
    author = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.title

