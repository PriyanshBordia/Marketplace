from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator

from django.contrib.auth.models import User

from datetime import datetime

# Create your models here.

class Tag(models.Model):

	name = models.CharField(max_length=64, blank=False, null=False)

	domain = models.CharField(max_length=64, blank=False, null=False, default="General")
	description = models.TextField(max_length=255, blank=False, null=False, default="A Tag")

	def isValidTag(self):
		return len(self.name) > 0

	def __str__(self):
		return f"{self.name}"


class Article(models.Model):

	title = models.CharField(validators=[MinLengthValidator(1)], max_length=64, blank=False, null=False, default="Article")

	description = models.TextField(max_length=255, blank=False, null=False, default="Describe the article...")

	image = models.ImageField(upload_to="images/", blank=False, null=False)

	price = models.FloatField(validators=[MinValueValidator(1)], blank=False, null=False)

	tags = models.ManyToManyField(Tag, blank=True, related_name="tags")

	def isValidArticle(self):
		return len(self.title) > 0 and self.price > 0

	def __str__(self):
		return f"{self.title} {self.price}"


class Person(models.Model):

	options = (('M', 'Male'), ('F', 'Female'), ('X', 'Not Preferred to say'))

	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")

	username = models.CharField(max_length=64, blank=False, null=False, unique=True)
	bio = models.TextField(max_length=500, blank=True, null=False)

	first = models.CharField(max_length=64, blank=False, null=False)
	last = models.CharField(max_length=64, blank=True, null=False)

	age = models.IntegerField(validators=[MinValueValidator(1)], blank=False, null=False, default=1)
	sex = models.CharField(max_length=1, choices=options, blank=False, null=False, default='X')
	
	email = models.EmailField(blank=False, null=False, unique=True)
	ph_no = models.BigIntegerField(blank=False, null=False, unique=True)

	rented = models.ManyToManyField(Article, blank=True, related_name="rented")
	bought = models.ManyToManyField(Article, blank=True, related_name="purchased")

	sold = models.ManyToManyField(Article, blank=True, related_name="sold")
	
	cart = models.ManyToManyField(Article, blank=True, related_name="cart")

	bookmarked = models.ManyToManyField(Article, blank=True, related_name="bookmarked")

	following = models.ManyToManyField('self', blank=True, related_name="following")

	allowsMessage = models.BooleanField(null=False, default=True)

	def isValidPerson(self):
		return self.rented != self.sold

		
	def __str__(self):
		return f"{self.first} {self.last}  {self.age}  {self.sex}"
	

class Message(models.Model):

	sender = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="send")

	receiver = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="receive")

	text = models.TextField(max_length=255, blank=False, null=False, default="Message")

	timestamp = models.DateTimeField(blank=False, null=False, default=datetime.now)
	
	def isValidMessage(self):
		return len(self.text) > 0 and (self.timestamp <= datetime.now)

	def __format__(self):
		return f"{self.sender} -> {self.receiver}"

	def __str__(self):
		return f"{self.timestamp}"
