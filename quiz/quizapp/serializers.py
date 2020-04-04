
from rest_framework import serializers
from .models import *

class QuizListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        field = {'id', 'quiz_id', 'quiz_title', }