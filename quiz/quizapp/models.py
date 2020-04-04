from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class QuizUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.IntegerField()
    

class Quiz(models.Model):
    quiz_id = models.CharField(max_length=32)
    quiz_title = models.CharField(max_length=32)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    questions = models.CharField(blank=False, max_length=256)
    score = models.FloatField(default=1)


class Option(models.Model):
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)


class Answers(models.Model):
    user = models.ForeignKey(QuizUser, on_delete=models.CASCADE)
    answers = models.ForeignKey(Option, on_delete=models.CASCADE)
