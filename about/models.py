from django.db import models
from reviews.models import Review
from ckeditor.fields import RichTextField

class Company(models.Model):
    name = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=200, unique=True)
    address = models.CharField(max_length=300)
    twitter_link = models.CharField(max_length=200, default="#")
    fb_link = models.CharField(max_length=200, default="#")
    instagram_link = models.CharField(max_length=200, default="#")
    history = RichTextField()
    school_info = RichTextField()
    number_of_students = models.IntegerField()
    number_of_awards = models.IntegerField()
    promotion_video = models.CharField(max_length=200, default="#")
    reviews = models.ManyToManyField(Review)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name