from django.db import models

# Create your models here.
from django.utils.text import slugify


class prove(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=200, null=False, blank=False)
    occupation = models.CharField(max_length=200, null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=False)
    state = models.CharField(max_length=200, null=False, blank=False)
    country = models.CharField(max_length=200, null=False, blank=False)
    option = models.CharField(max_length=200, null=False, blank=False)
    sub = models.FileField()

    def __str__(self):
        return self.name

class grate(models.Model):
    caption = models.CharField(max_length=200)
    image = models.FileField(upload_to="img/%y")
    def __str__(self):
        return self.caption

class hmm(models.Model):
    caption = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    hes = models.CharField(max_length=200)
    main_news = models.CharField(max_length=400)
    def __str__(self):
        return self.caption

