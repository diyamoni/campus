from django.db import models

class LostItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date_lost = models.DateField()
    contact_info = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class FoundItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date_found = models.DateField()
    contact_info = models.CharField(max_length=200)

    def __str__(self):
        return self.title
