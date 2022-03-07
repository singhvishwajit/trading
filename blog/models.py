from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
	category_name = models.CharField(max_length=100)
	category_details = models.CharField(max_length=100)
	slug = models.SlugField(default="some-string")

	# add in thumbnail

	def __str__(self):
		return f"{self.id} - {self.category_name}"



class Investing(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	details = models.TextField(default='hello')
	slug = models.SlugField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	thumbnail = models.ImageField(default='default.png', blank=True)

	# add in thumbnail, category

	def __str__(self):
		return self.title

	def snippet(self):
		return self.content[:200]


class Contact(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	subject = models.CharField(max_length=100)
	message = models.TextField()		

	def __str__(self):
		return self.name

class Research(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	details = models.TextField(default='hello')
	slug = models.SlugField()
	categories = models.ManyToManyField(Category, blank=True)
	thumbnail = models.ImageField(default='default.png', blank=True)
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	thumbnail = models.ImageField(default='default.png', blank=True)
	alt_text = models.TextField(default="some-string")

	# add in thumbnail, category

	def __str__(self):
		return self.title

	def snippet(self):
		return self.content[:200]


class Protocol(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	details = models.TextField(default='hello')
	slug = models.SlugField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	thumbnail = models.ImageField(default='default.png', blank=True)

	# add in thumbnail, category

	def __str__(self):
		return self.title

	def snippet(self):
		return self.content[:200]


