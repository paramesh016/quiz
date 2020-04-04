from rest_framework import generics
from .models import *
from quizapp import serializers as quiz_serializers
from rest_framework.views import APIView


class QuizListAPI(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = quiz_serializers.QuizListSerializer



class SubmitAPI(generics.ListAPIView):
    query_set = Question.objects.all()
    serializer_class = quiz_serializers.QuestionOptionSerializer



class RightWrongAPI(APIView):

    def post(self, request, format=None):
        answers = {'answered': '', 'correct-answer': ''}
        question_id = request.POST.get('question_id', '')
        question = Question.objects.filter(id=question_id)
        if question:
            answered = Answers.objects.filter(question__id=question_id)
            option = Option.objects.filter(questions__id=question_id, is_correct=True)
            if answered:
                answers.update({'answered': answered[0].option})
            if option:
                answers.update({'correct_answer': option[0].option})
        return answers

