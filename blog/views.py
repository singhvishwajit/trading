from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post, DeFi, Project, Contact, Investment
from django.views.generic import ListView, DetailView, CreateView

def home(request):
	context = {
		'posts': Post.objects.all() [:4]
	}
	return render(request, 'blog/home.html', context)

# def about(request):
# 	return render(request, 'blog/about.html', {'title': 'About'})

# def projects(request):
# 	return render(request, 'blog/projects.html', {'title': 'Projects'})

def resources(request):
	return render(request, 'blog/resources.html', {'title': 'Resources'})

class PostDetailView(DetailView):
	model = Post

class DeFiDetailView(DetailView):
	model = DeFi

class ProjectDetailView(DetailView):
	model = Project

class InvestmentDetailView(DetailView):
	model = Investment

class ContactCreateView(CreateView):
    model = Contact
    fields = ['name', 'email', 'subject', 'message']
    success_url = 'success'

def ContactSuccess(request):
	return render(request, 'blog/contact_success.html', {'title': 'Contact'})

# def articles(request):
# 	context = {
# 		'posts': Post.objects.all(),
# 		'title': 'Notes'
# 	}
# 	return render(request, 'blog/articles.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'blog/articles.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 6
	def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        	context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        	
        	context['title'] = 'Learn'
        	return context


class DeFiListView(ListView):
	model = DeFi
	template_name = 'blog/defi.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'defis'
	ordering = ['-date_posted']
	paginate_by = 6
	def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        	context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        	
        	context['title'] = 'Learn'
        	return context

class ProjectListView(ListView):
	model = Project
	template_name = 'blog/projects.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'projects'
	ordering = ['-date_posted']
	paginate_by = 6
	def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        	context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        	
        	context['title'] = 'Learn'
        	return context

class InvestmentListView(ListView):
	model = Investment
	template_name = 'blog/investment.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'investments'
	ordering = ['-date_posted']
	paginate_by = 6
	def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        	context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        	
        	context['title'] = 'Learn'
        	return context