from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Investing, Research, Protocol, Contact
from django.views.generic import ListView, DetailView, CreateView

def home(request):
	# context = {
	# 	'tradings': Trading.objects.all() [:4]
	# }
	return render(request, 'blog/home.html')

def resources(request):
	return render(request, 'blog/resources.html', {'title': 'Resources'})

def privacy(request):
	return render(request, 'blog/privacy.html', {'title': 'Privacy'})

def terms(request):
	return render(request, 'blog/terms.html', {'title': 'Terms of Use'})


class InvestingDetailView(DetailView):
	model = Investing

class ResearchDetailView(DetailView):
	model = Research

class ProtocolDetailView(DetailView):
	model = Protocol

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

class InvestingListView(ListView):
	model = Investing
	template_name = 'blog/investing.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'investings'
	ordering = ['-date_posted']
	paginate_by = 6
	def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        	context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        	
        	context['title'] = 'Investing'
        	return context


class ResearchListView(ListView):
	model = Research
	template_name = 'blog/research.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'researches'
	ordering = ['-date_posted']
	paginate_by = 6
	def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        	context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        	
        	context['title'] = 'Research'
        	return context

class ProtocolListView(ListView):
	model = Protocol
	template_name = 'blog/protocol.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'protocols'
	ordering = ['-date_posted']
	paginate_by = 6
	def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        	context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        	
        	context['title'] = 'Protocols'
        	return context
