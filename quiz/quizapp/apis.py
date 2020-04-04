from rest_framework import generics
from .models import *
from quizapp import serializers as quiz_serializers


class QuizListAPI(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = quiz_serializers.QuizListSerializer

