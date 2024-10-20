from django.shortcuts import render

from .models import Book

def home(request):
  return render(request, 'home.html')

def book(request):
  books = Book.objects.all()

  return render(request, 'books/book.html', {'books': books})