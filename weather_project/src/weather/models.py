from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def str(self):
        return self.name
