from django.db import models
from autoslug import AutoSlugField
from blog.models import CatagoryModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from blog.abstract_models import DateAbstractModel


class ArticleModel(DateAbstractModel):
    articleImage = models.ImageField(upload_to="article_images")
    title = models.CharField(max_length=50)
    content = RichTextField()
    slug = AutoSlugField(populate_from="title", unique=True)
    categories = models.ManyToManyField(CatagoryModel, related_name="article")
    author = models.ForeignKey(
        "account.CustomUserModel", on_delete=models.CASCADE, related_name="articles")

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        db_table = "Article"

    def __str__(self):
        return self.title
