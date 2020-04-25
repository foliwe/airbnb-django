from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    """ Time Stamps Model """

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        abstract = True  # Abstract model does not go to the database
