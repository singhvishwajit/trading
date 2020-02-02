from django.urls import path, include
from .views import PostDetailView, ContactCreateView, NewsletterCreateView
from . import views


urlpatterns = [
	path('', views.home, name='blog-home'),
	path('about/', views.about, name='blog-about'),
	path('articles/', views.articles, name='blog-articles'),
	path('post/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
	path('newsletter/', NewsletterCreateView.as_view(), name='blog-newsletter'),
	path('services/', views.services, name='blog-services'),
	path('contact/', ContactCreateView.as_view(), name='blog-contact'),
	path('contact/success', views.ContactSuccess, name='blog-contact-success'),
	path('tinymce/', include('tinymce.urls')),
]