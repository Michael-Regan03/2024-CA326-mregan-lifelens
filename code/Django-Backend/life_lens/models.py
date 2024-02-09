from django.db import models
from users.models import UserAccount
from life_lens.lifelogDataMapping import action, actionOption, actionSub, actionSubOption, condition, conditionSub1Option, conditionSub2Option, activity, place
from django.core.validators import MinValueValidator, MaxValueValidator

class Day(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    days = models.IntegerField()
    
    #Throughning errors // needs fixing or new approach
    #class Meta:
    #    unique_together = [['user', 'days']]

class DailyActivities(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE) #Primary key
    ts = models.FloatField()  # Assuming it's a timestamp represented as a float
    action = models.CharField(max_length=100, choices=action)
    actionOption = models.IntegerField(choices=actionOption)
    actionSub = models.CharField(max_length=100, choices=actionSub, null=True, blank=True)  # Nullable
    actionSubOption = models.FloatField(choices=actionSubOption, null=True, blank=True)  # Nullable
    condition = models.CharField(max_length=100, choices=condition)
    conditionSub1Option = models.IntegerField(choices=conditionSub1Option , null=True, blank=True)  # Nullable
    conditionSub2Option = models.IntegerField(choices=conditionSub2Option , null=True, blank=True)  # Nullable
    place = models.CharField(max_length=100, choices=place)
    emotionPositive = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)])
    emotionTension = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)])
    activity = models.IntegerField(choices=activity)

