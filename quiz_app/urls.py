from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.user_login, name='user_login'),  # Redirect to login page by default
    path('quiz-list/', views.quiz_list, name='quiz_list'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('quiz/<int:quiz_id>/answer/', views.quiz_answer, name='quiz_answer'),
    path('result/<int:result_id>/', views.quiz_result, name='quiz_result'),
    path('login/', views.user_login, name='user_login'),
]
