
from rest_framework import serializers
from .models import *

class QuizListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = ('quiz_title',)


class QuestionOptionSerializer(serializers.ModelSerializer):
    quiz_id = serializers.CharField(source='quiz.quiz_id', read_only=True)
    quiz_title = serializers.CharField(source='quiz.title', read_only=True)
    options = serializers.SerializerMethodField('_get_options', read_only=True)

    class Meta:
        model = Question
        fields  = ('id', 'quiz_id', 'quiz_title')

    
    def _get_options(self, obj):
        option_list = []
        opt_dict = {'id':'', 'option': '', 'is_correct': ''}
        details_obj = Option.objects.filter(question=obj)
        if details_obj:
            for option in details_obj:
                opt_dict.update({'id': option.id, 'option': option.option, 'is_correct': option.is_correct})
                option_list.append(opt_dict)
        return option_list


class SubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ('user', 'answer', 'question')
