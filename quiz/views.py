from .permissions import IsStuffOrReadOnly
from .models import Questions, Quiz
from .serializers import QuestionSerializer, QuestionsAll, QuizSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class QuizView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = (IsStuffOrReadOnly,)

class Question(generics.ListAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsAll
    permission_classes = (IsStuffOrReadOnly,)

class QuizQuestion(APIView):
    def get(self, request, format=None, **kwargs):
        quiz = Questions.objects.filter(quiz__name=kwargs['name'])
        serializer = QuestionSerializer(quiz,many = True)
        return Response(serializer.data)