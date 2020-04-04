from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class QuizUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.IntegerField(max_length=2)
    

class Quiz(models.Model):
    quiz_id = models.CharField(max_length=32)
    quiz_title = models.CharField(max_length=32)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz)
    questions = models.CharField(blank=False)
    score = models.FloatField(default=1)


class Option(models.Model):
    questions = models.ForeignKey(Question)
    option = models.ForeignKey(quiz)
    is_correct = models.BooleanField(default=False)


class Answers(models.Model):
    user = models.ForeignKey(QuizUser)
    answers = models.ForeignKey(Option)
