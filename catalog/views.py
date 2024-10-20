from django.shortcuts import render

from .models import *

def home(request):
  return render(request, 'home.html')

def book(request):
  books = Book.objects.all()

  return render(request, 'books/book.html', {'books': books})

def authors(request):
  authors = Author.objects.all()

  return render(request, 'authors/author.html', {'authors': authors})