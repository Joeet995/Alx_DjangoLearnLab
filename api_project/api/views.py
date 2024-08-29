from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListCreateAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer