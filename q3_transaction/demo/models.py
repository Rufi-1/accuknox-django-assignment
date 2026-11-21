from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Log(models.Model):
    # the signal receiver will create a row in this table
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.message
