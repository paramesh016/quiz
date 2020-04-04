from rest_framework import generics
from .models import *
from quizapp import serializers as quiz_serializers
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from rest_framework import status

class QuizListAPI(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = quiz_serializers.QuizListSerializer


class SubmitAPI(generics.ListCreateAPIView):
    query_set = Answers.objects.all()
    serializer_class = quiz_serializers.QuestionOptionSerializer



class RightWrongAPI(APIView):

    def get(self, request, format=None):
        answers = {'answered': '', 'correct-answer': ''}
        question_id = request.GET.get('question_id', '')
        question = Question.objects.filter(id=question_id)
        if question:
            answered = Answers.objects.filter(question__id=question_id)
            option = Option.objects.filter(questions__id=question_id, is_correct=True)
            if answered:
                answers.update({'answered': answered[0].option})
            if option:
                answers.update({'correct_answer': option[0].option})
        return JsonResponse(answers, status=status.HTTP_202_ACCEPTED, safe=False)



class ScoreApi(APIView):
    def get(self, request, format=None):
        score = 0
        user_id = request.GET.get('user_id', '')
        question = request.GET.get('question', '')
        answers = Answers.objects.filter(user__id=user_id, question=question)
        for answer in answers:
            if answer.is_correct:
                score =+ answer.question.score
        return JsonResponse(score, status=status.HTTP_202_ACCEPTED, safe=False)


class ScoreCsvApi(APIView):
    def get(self, request, format=None):
        fname = "user_score.csv"
        loc = '/quiz/quizapp/' + 'csv_files/'
        filename = fname
        _fname = '%s%s' % (loc, filename)
        with open(_fname, 'w', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['User', 'Question', 'Answer', 'score'])
            csv_data = []
            answers = Answers.objects.all()\
                .values_list('user__user_id','question__question' ,'answers__option', 'question__score',)
            for i in answers:
                data = [i]
                csv_data.append(data)
            csvwriter.writerows(csv_data)
