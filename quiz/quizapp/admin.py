from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Answers)
admin.site.register(Quiz)
admin.site.register(QuizUser)


