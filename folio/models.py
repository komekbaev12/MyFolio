from django.db import models


class Companies(models.Model):
    image = models.ImageField(upload_to='media/', blank=True, null=True)

class Services(models.Model):
    services_title = models.CharField(max_length=100)
    services_price = models.CharField(max_length=50)
    services_description = models.TextField()

class Projects(models.Model):
    projects_title = models.CharField(max_length=100)
    projects_subtitle = models.CharField(max_length=100)
    projects_image = models.ImageField(upload_to='media/', blank=True, null=True)
