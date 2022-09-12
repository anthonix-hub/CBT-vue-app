from django.db import models


class QuestLog(models.Model):
    question = models.CharField(max_length=50)
    answers = models.CharField(max_length=50)
    opts = models.CharField(max_length=50)


class ansChoosed(models.Model):
    quest = models.OneToOneField(QuestLog, on_delete=models.CASCADE)
    choice = models.CharField(max_length=50)
