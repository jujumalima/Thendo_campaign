from django.db import models

"""
Models for the Home application.

This module defines the data models for news articles and events, 
used on the home page to display the latest news and upcoming events.
"""

class News(models.Model):
    """
    Represents a news article.

    Attributes:
        title (str): The title of the news article.
        content (str): The main content of the news article.
        published_date (datetime): The date and time when the article was published.
        image (ImageField): An optional image associated with the news article.
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='static/img/news/', null=True, blank=True) 

    def __str__(self):
        """
        Returns the string representation of the News object.

        Returns:
            str: The title of the news article.
        """
        return self.title


class Event(models.Model):
    """
    Represents an event.

    Attributes:
        name (str): The name of the event.
        date (date): The scheduled date of the event.
        location (str): The location where the event will take place.
        image (ImageField): An optional image associated with the event.
    """
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/img/events/', null=True, blank=True)  

    def __str__(self):
        """
        Returns the string representation of the Event object.

        Returns:
            str: The name of the event.
        """
        return self.name
