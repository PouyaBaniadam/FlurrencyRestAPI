from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=50, unique=True)
    persian_name = models.CharField(max_length=50, unique=True)
    is_allowed = models.BooleanField(default=True)

    def __str__(self):
        return self.name
