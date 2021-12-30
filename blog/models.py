from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Trading(models.Model):
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

class DeFi(models.Model):
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


class Project(models.Model):
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


class Investment(models.Model):
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
