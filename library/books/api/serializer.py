from rest_framework import serializers
from books import models

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ['id_book', 'title', 'author', 'realise_year', 'state', 'pages', 'publishing_company', 'create_at']