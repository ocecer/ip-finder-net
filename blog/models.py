from distutils.command.upload import upload
from sre_parse import CATEGORIES
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blog_images")
    description = RichTextField()
    is_verified = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True)
    # category = models.ForeignKey(Category, default=1, on_delete=models.SET_DEFAULT)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
