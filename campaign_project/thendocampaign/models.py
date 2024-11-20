from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='static/img/news/', null=True, blank=True) 

    def __str__(self):
        return self.title

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/img/events/', null=True, blank=True)  

    def __str__(self):
        return self.name