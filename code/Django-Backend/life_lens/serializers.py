from rest_framework import serializers
from life_lens.models import DailyActivities, Day


class CSVUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

class DailyActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyActivities
        fields = [
                'emotionPositive',
                'emotionTension'
        ]

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = [
                'days'
        ] 