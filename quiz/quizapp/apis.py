from rest_framework import generics
from .models import *
from quizapp import serializers as quiz_serializers


class QuizListAPI(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = quiz_serializers.QuizListSerializer

