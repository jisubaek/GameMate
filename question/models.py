from django.db import models
from django.utils import timezone

class Game(models.Model):
    title1 = models.CharField(max_length=100)
    title2 = models.CharField(max_length=100)
    title3 = models.CharField(max_length=100)
    peoplenum = models.CharField(max_length=100)
    playrule = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    # 추가 필드들...

    def __str__(self):
        return f"{self.title1}, {self.title2}"
