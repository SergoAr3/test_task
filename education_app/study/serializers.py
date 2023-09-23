from rest_framework import serializers
from .models import Lesson, CheckView



class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CheckViewSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()

    class Meta:
        model = CheckView
        fields = ('lesson', 'status', 'watched_time_seconds')