from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MinLengthValidator

from datetime import datetime

from django.contrib.auth.models import User


# Create your models here.

class Tag(models.Model):

	name = models.CharField(max_length=64, blank=False, null=False)

	domain = models.CharField(max_length=64, blank=False, null=False, default="General")

	description = models.TextField(max_length=511, blank=False, null=False, default="A Tag")

	# slug = models.SlugField()

	# def save(self, *args, **kwargs):
	# 	super.save(args, kwargs)


	def isValidTag(self):
		return len(self.name) > 0

	def __str__(self):
		return f"{self.name}"


class Article(models.Model):

	title = models.CharField(validators=[MinLengthValidator(1)], max_length=64, blank=False, null=False, default="Article")

	description = models.TextField(max_length=255, blank=False, null=False, default="Describe the article...")

	image = models.ImageField(upload_to="images/", blank=False, null=False)

	# pub_date = models.DateTimeField(blank=False, null=False, default=datetime.now)

	price = models.FloatField(validators=[MinValueValidator(1)], blank=False, null=False)

	tags = models.ManyToManyField(Tag, blank=True, related_name="tags")

	# slug = models.SlugField()

	def __get_image_name__(self):
		date = datetime.now(datetime.timezone.utc)
		year = str(date.year)
		month = date.month
		day = date.day

		if month <= 9:
			month = '0' + str(month)
		if day <= 9:
			day = '0' + str(day)

		self.image_name = 'Image_' + date.strftime("%Y-%m-%d_at_%H.%M.%S")

		# str(year) + '-' + str(month) + '-' + str(day) + 

	# def save(self, *args, **kwargs):
	# 	self.slug = slugify(self.tittle)
	# 	self.image_name = self.get_image_name();
	# 	super(Article, self).save(*args, **kwargs)

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
	display = models.ManyToManyField(Article, blank=True, related_name="display")

	cart = models.ManyToManyField(Article, blank=True, related_name="cart")

	bookmarked = models.ManyToManyField(Article, blank=True, related_name="bookmarked")

	friends = models.ManyToManyField('self', blank=True, related_name="friends")

	allowsMessage = models.BooleanField(null=False, default=True)

	def isValidPerson(self):
		return self.rented != self.sold

		
	def __str__(self):
		return f"{self.first} {self.last}  {self.age}  {self.sex}"
	

class Message(models.Model):

	text = models.TextField(max_length=255, blank=False, null=False, default="Message")

	timestamp = models.DateTimeField(blank=False, null=False, default=datetime.now)
	
	def isValidMessage(self):
		return len(self.text) > 0 and (self.timestamp <= datetime.now)

	def __format__(self):
		return f"{self.sender} -> {self.receiver}"

	def __str__(self):
		return f"{self.timestamp}"


class Chat(models.Model):
	
	sender = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="sender")

	receiver = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="receiver")

	messages = models.ManyToManyField(Message, blank=True, related_name="messages")
	
	# timestamp = models.DateTimeField(blank=False, null=False, default=datetime.now)

	slug = models.SlugField()

	def __format__(self):
		return f"{self.sender} <-> {self.receiver}"

	def __str__(self):
		return f"{self.timestamp}"
