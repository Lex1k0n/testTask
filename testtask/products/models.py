from django.db import models


class Product(models.Model):

    title = models.CharField(max_length=30)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    start_date = models.DateField()

    def __str__(self):
        return self.title
