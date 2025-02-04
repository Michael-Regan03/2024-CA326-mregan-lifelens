from django.db import models
from users.models import UserAccount
from life_lens.lifelogDataMapping import actionOption,  actionSubOption, condition, conditionSub1Option, conditionSub2Option, activity, place, sleep, sleepProblem, dream, amCondition, amEmotion, pmStress_Fatigue, alcoholType
from django.core.validators import MinValueValidator, MaxValueValidator

class Day(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    date = models.DateField()
    days = models.IntegerField()

class DailyActivity(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    action = models.IntegerField(choices=actionOption)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    duration = models.TimeField()

class SubOption(models.Model):
    dailyActivity = models.ForeignKey(DailyActivity, on_delete=models.CASCADE)
    actionSubOption = models.CharField(max_length=100,choices=actionSubOption)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    duration = models.TimeField()

class Condition(models.Model):
    dailyActivity = models.ForeignKey(DailyActivity, on_delete=models.CASCADE)
    condition = models.CharField(max_length=100,choices=condition)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    duration = models.TimeField()

class ConditionSub1Option(models.Model):
    dailyActivity = models.ForeignKey(DailyActivity, on_delete=models.CASCADE)
    conditionSub1Option = models.IntegerField(choices=conditionSub1Option)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    duration = models.TimeField()

class ConditionSub2Option(models.Model):
    dailyActivity = models.ForeignKey(DailyActivity, on_delete=models.CASCADE)
    conditionSub2Option = models.IntegerField(choices=conditionSub2Option)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    duration = models.TimeField()

class Place(models.Model):
    dailyActivity = models.ForeignKey(DailyActivity, on_delete=models.CASCADE)
    place = models.CharField(max_length=100,choices=place)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    duration = models.TimeField()

class EmotionPositive(models.Model):
    dailyActivity = models.ForeignKey(DailyActivity, on_delete=models.CASCADE)
    emotionPositive = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)])
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    duration = models.TimeField()

class EmotionTension(models.Model):
    dailyActivity = models.ForeignKey(DailyActivity, on_delete=models.CASCADE)
    emotionTension = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)])
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    duration = models.TimeField()

class Activity(models.Model):
    dailyActivity = models.ForeignKey(DailyActivity, on_delete=models.CASCADE)
    activity = models.IntegerField(choices=activity)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    duration = models.TimeField()



#######  Survey Data


class SurveyAM(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    sleep = models.IntegerField(choices=sleep)
    sleepProblem = models.IntegerField(choices=sleepProblem)
    dream = models.IntegerField(choices=dream)
    condition = models.IntegerField(choices=amCondition)
    emotion = models.IntegerField(choices=amEmotion)
    

class SurveyPM(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    emotion = models.IntegerField(choices=amEmotion)
    stress = models.IntegerField(choices=pmStress_Fatigue)
    fatigue = models.IntegerField(choices=pmStress_Fatigue)
    caffeine = models.CharField(max_length=100)
    cAmount = models.IntegerField()
    alcohol = models.IntegerField(choices=alcoholType)
    aAmount = models.IntegerField()


class Illness(models.Model):
    name = models.CharField(max_length=255)
    shortCode = models.CharField(max_length=50)
    url = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        #makes it easier for admin
        return self.name

