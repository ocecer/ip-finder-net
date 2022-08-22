from django.db import models


class DateAbstractModel(models.Model):
    creationDate = models.DateTimeField(auto_now_add=True)
    editDate = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
