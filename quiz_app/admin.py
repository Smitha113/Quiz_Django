from django.contrib import admin
from .models import Topic, Quiz, Question, Answer, QuizResult

admin.site.register(Topic)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuizResult)
