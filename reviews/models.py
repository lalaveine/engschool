from django.db import models

class Review(models.Model):
    reviewer_name = models.CharField(max_length=200)
    review_text = models.CharField(max_length=500)
    reviewer_image =  models.ImageField(upload_to='reviews')
    position = models.CharField(max_length=200)

    def __str__(self):
        return self.reviewer_name