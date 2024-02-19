from django.contrib import admin
from .models import Day, DailyActivity, SubOption, Condition, ConditionSub1Option, ConditionSub2Option, Place, EmotionPositive, EmotionTension, Activity, SurveyAM, SurveyPM, Illness




admin.site.register(Day)
admin.site.register(DailyActivity)
admin.site.register(SubOption)
admin.site.register(Condition)
admin.site.register(ConditionSub1Option)
admin.site.register(ConditionSub2Option)
admin.site.register(Place)
admin.site.register(EmotionPositive)
admin.site.register(EmotionTension)
admin.site.register(Activity)

admin.site.register(SurveyAM)
admin.site.register(SurveyPM)

admin.site.register(Illness)
