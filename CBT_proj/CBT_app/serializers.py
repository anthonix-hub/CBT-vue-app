from rest_framework import serializers
from .models import QuestLog, ansChoosed


class QuestionLogSerialiser(serializers.ModelSerializer):
    class Meta:
        model = QuestLog
        fields = (
            'question',
            'answers',
            'opts'
        )

class ansChoosedSerialiser(serializers.ModelSerializer):
    class Meta:
        model = ansChoosed
        fields = (
            'quest',
            'choice'
        )
