from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class DailyActivities(models.Model):
    ts = models.FloatField()  # Assuming it's a timestamp represented as a float
    action = models.CharField(max_length=100)
    actionOption = models.IntegerField()
    actionSub = models.CharField(max_length=100, null=True, blank=True)  # Nullable
    actionSubOption = models.FloatField(null=True, blank=True)  # Nullable
    condition = models.CharField(max_length=100)
    conditionSub1Option = models.FloatField(null=True, blank=True)  # Nullable
    conditionSub2Option = models.FloatField(null=True, blank=True)  # Nullable
    place = models.CharField(max_length=100)
    emotionPositive = models.IntegerField()
    emotionTension = models.IntegerField()
    activity = models.IntegerField()

