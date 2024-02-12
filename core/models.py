from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):

    title = models.CharField(max_length = 255)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.title
