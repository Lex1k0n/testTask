from django.db import models
import datetime
from django.contrib.auth.models import User


class ProductModel(models.Model):

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50, default='admin')
    starttime = models.DateTimeField(default=datetime.datetime.now())
    price = models.IntegerField(default=0)
    group_count = models.IntegerField(default=1)
    min_part = models.IntegerField(default=1)
    max_part = models.IntegerField(default=1)

    def __str__(self):
        return self.title


class AccessModel(models.Model):

    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        ret = str(self.product) + ': ' + str(self.user)
        return ret


class LessonModels(models.Model):

    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    ref = models.URLField(max_length=200)

    def __str__(self):
        return self.title


class GroupModel(models.Model):

    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    number = models.IntegerField()

    def __str__(self):
        ret = str(self.product) + ': ' + str(self.number)
        return ret


class GroupMembers(models.Model):

    group = models.ForeignKey(GroupModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
