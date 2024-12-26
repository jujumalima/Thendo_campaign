from django.db import models

"""
Models for the Donations application.

This module defines the data structure for managing newsletter subscribers.
"""

class NewsletterSubscriber(models.Model):
    """
    Represents a subscriber to the newsletter.

    Attributes:
        name (str): The name of the subscriber.
        email (str): The email address of the subscriber. Must be unique.
        subscribed_at (datetime): The date and time when the subscriber signed up.
    """
    name = models.CharField(max_length=100, help_text="Name of the subscriber.")
    email = models.EmailField(unique=True, help_text="Unique email address of the subscriber.")
    subscribed_at = models.DateTimeField(auto_now_add=True, help_text="Date and time of subscription.")

    def __str__(self):
        """
        Returns a string representation of the subscriber.
        """
        return f"{self.name} ({self.email})"
