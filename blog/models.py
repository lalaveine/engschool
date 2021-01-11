from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from ckeditor.fields import RichTextField
from hitcount.models import HitCountMixin, HitCount

# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model, HitCountMixin):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content =  RichTextField()
    content_preview = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    title_image = models.ImageField(upload_to='blog')
    
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title