from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponse
from django.utils import timezone

from .models import Book

# class forms


# Create your views here.
def index(request):
	return render(request, 'pontoApp/index.html')

def books(request):
	books = Book.objects.filter(date=timezone.now()).order_by('-id').all()
	return render(request, 'pontoApp/book/index.html', {'books': books})

def report(request):
	if request.method == 'POST':
		books = Book.objects.filter(date__range=(request.POST['dateSelectedFrom'], request.POST['dateSelectedTo'])).order_by('-id').all()
		return render(request, 'pontoApp/book/report.html', {'books': books, 'dateSelectedFrom': request.POST['dateSelectedFrom'], 'dateSelectedTo' : request.POST['dateSelectedTo']})

	return render(request, 'pontoApp/book/report.html')

def register(request):
	if request.method == 'POST':
		Book.objects.create()
	books = Book.objects.order_by('-id').all()
	return redirect('/books', {'books': books})

	
		
	