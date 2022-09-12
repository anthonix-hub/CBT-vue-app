from django.shortcuts import render
from rest_framework import generics
from .serializers import QuestionLogSerialiser, ansChoosedSerialiser
from .models import QuestLog, ansChoosed


def index(reqeest):

    return render(reqeest, 'CBT_app/index.html', None)

class QuestionList(generics.ListCreateAPIView):
    queryset = QuestLog.objects.all()
    serializer_class = QuestionLogSerialiser

class QuestionDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuestLog.objects.all()
    serializer_class = QuestionLogSerialiser
