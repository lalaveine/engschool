from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=200)
    description = RichTextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    duration = models.CharField(max_length=200)
    number_of_seats = models.IntegerField()
    promote_image = models.ImageField(upload_to='courses')

    def __str__(self):
        return self.name