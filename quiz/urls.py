from django.urls import path
from .views import Question, QuizQuestion, QuizView



urlpatterns = [
     path('',QuizView.as_view(),name='quiz'),
     path('q/',Question.as_view(),name='question'),
     path('q/<str:name>/',QuizQuestion.as_view(),name='quizquestion'),
  
]
