from rest_framework import serializers
from .models import book, review

class review_serializer(serializers.ModelSerializer):
    class Meta:
        model = review
        fields = '__all__'


class book_serializer(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = '__all__'