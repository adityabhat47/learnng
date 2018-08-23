from .models import Learning
from rest_framework import serializers

class learningSerializer(serializers.ModelSerializer):
    class Meta:
        model=Learning
        fields=("language","category","difficulty","words")
# category=models.CharField(max_length=20)
# difficulty=models.CharField(max_length=20)
# words=models.CharField(max_length=20)