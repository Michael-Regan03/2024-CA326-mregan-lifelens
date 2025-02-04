from rest_framework import serializers
from .models import Day, DailyActivity, SubOption, Condition, ConditionSub1Option, ConditionSub2Option, Place, EmotionPositive, EmotionTension, Activity, Illness

class CSVUploadSerializer(serializers.Serializer):
        file = serializers.FileField()

class DailyActivitySerializer(serializers.ModelSerializer):
        action_label = serializers.SerializerMethodField()
        class Meta:
                model = DailyActivity
                fields = [
                        'action',
                        'action_label',
                        'startTime',
                        'endTime',
                        'duration'
                ]
        #Decoding the action field from int to human readable value
        def get_action_label(self, obj):
                return obj.get_action_display()
        


class DaySerializer(serializers.ModelSerializer):
        class Meta:
                model = Day
                fields = [
                        'date'
                ]

class SubOptionSerialiser(serializers.ModelSerializer):
        class Meta:
                model = SubOption
                fields = [
                        'actionSubOption', 
                        'startTime',
                        'endTime',
                        'duration'
                ]

class ConditionSerialiser(serializers.ModelSerializer):
        class Meta:
                model = Condition
                fields = [
                        'condition', 
                        'startTime',
                        'endTime',
                        'duration'
                ]

class ConditionSub1OptionSerialiser(serializers.ModelSerializer):
        conditionSub1Option_label = serializers.SerializerMethodField()
        class Meta:
                model = ConditionSub1Option
                fields = [
                        'conditionSub1Option',
                        'conditionSub1Option_label',
                        'startTime',
                        'endTime',
                        'duration'
                ]
                
        def get_conditionSub1Option_label(self, obj):
                return obj.get_conditionSub1Option_display()

class ConditionSub2OptionSerialiser(serializers.ModelSerializer):
        conditionSub2Option_label = serializers.SerializerMethodField()
        class Meta:
                model = ConditionSub2Option
                fields = [
                        'conditionSub2Option',
                        'conditionSub2Option_label',
                        'startTime',
                        'endTime',
                        'duration'
                ]

        def get_conditionSub2Option_label(self, obj):
                return obj.get_conditionSub2Option_display()
    
class EmotionTensionSerialiser(serializers.ModelSerializer):
        class Meta:
                model = EmotionTension
                fields = [
                        'emotionTension',
                        'startTime',
                        'endTime',
                        'duration'
                ]

class EmotionPositiveSerialiser(serializers.ModelSerializer):
        class Meta:
                model = EmotionPositive
                fields = [
                       'emotionPositive',
                       'startTime',
                        'endTime',
                        'duration'
                ]



class PlaceSerialiser(serializers.ModelSerializer):
        class Meta:
                model = Place
                fields = [
                        'place',
                        'startTime',
                        'endTime',
                        'duration'
                ]


class ActivitySerialiser(serializers.ModelSerializer):
        activity_label = serializers.SerializerMethodField()
        class Meta:
                model = Activity
                fields = [
                        'activity',
                        'activity_label',
                        'startTime',
                        'endTime',
                        'duration'
                ]
        def get_activity_label(self, obj):
                return obj.get_activity_display()


class IllnessSerialiser(serializers.ModelSerializer):
        class Meta:
                model = Illness
                fields = [
                        'name',
                        'url',
                        'description'
                ]