from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    amount = models.IntegerField()
    is_active = models.BooleanField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
