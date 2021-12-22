from django.urls import path, include
from .views import PostListView, PostDetailView, ContactCreateView, DeFiListView, DeFiDetailView, ProjectListView, ProjectDetailView, InvestmentListView, InvestmentDetailView
from . import views


urlpatterns = [
	path('', views.home, name='blog-home'),
	# path('about/', views.about, name='blog-about'),
	path('articles/', PostListView.as_view(), name="blog-articles"),
	path('defi/', DeFiListView.as_view(), name="blog-defi"),
	path('investment/', InvestmentListView.as_view(), name="blog-investment"),
	path('projects/', ProjectListView.as_view(), name="blog-projects"),
	path('resources/', views.resources, name='blog-resources'),
	path('post/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
	path('defi/<slug:slug>/', DeFiDetailView.as_view(), name='defi-detail'),
	path('investment/<slug:slug>/', InvestmentDetailView.as_view(), name='investment-detail'),
	path('project/<slug:slug>/', ProjectDetailView.as_view(), name='project-detail'),
	path('contact/', ContactCreateView.as_view(), name='blog-contact'),
	path('contact/success', views.ContactSuccess, name='blog-contact-success'),
	path('tinymce/', include('tinymce.urls')),
]