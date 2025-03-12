from rest_framework import serializers
from .models import Book, Author
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    name = BookSerializer(many = True, read_only =True)
    class Meta:
        model = Author
        fields = ['name','title', 'publication_year','author']
    def validate(self, attrs):
        if attrs['publication_year'] > date.day:
            raise serializers.ValidationError('The plublication year can not be in the future')
        return attrs