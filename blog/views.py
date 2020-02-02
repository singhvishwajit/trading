from django.shortcuts import render
from .models import Post, Contact, Newsletter
from django.views.generic import ListView, DetailView, CreateView

def home(request):
	context = {
		'posts': Post.objects.all() [:4]
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})

def services(request):
	return render(request, 'blog/services.html', {'title': 'Services'})

class PostDetailView(DetailView):
	model = Post

class ContactCreateView(CreateView):
    model = Contact
    fields = ['name', 'email', 'subject', 'message']
    success_url = 'success'

def ContactSuccess(request):
	return render(request, 'blog/contact_success.html')

def articles(request):
	context = {
		'posts': Post.objects.all(),
		'title': 'Notes'
	}
	return render(request, 'blog/articles.html', context)

class NewsletterCreateView(CreateView):
	model = Newsletter
	fields = ['email']