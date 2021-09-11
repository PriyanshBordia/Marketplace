from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MinLengthValidator

from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
	
	name = models.CharField(max_length=64, blank=False, null=False)

	domain = models.CharField(max_length=64, blank=False, null=False)

	description = models.TextField(max_length=511, blank=False, null=False)

	created_ts = models.DateTimeField(auto_now_add=True)
	updated_ts = models.DateTimeField(auto_now=True)

	slug = models.SlugField(max_length=64, blank=False, null=False, unique=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(str(Tag.objects.all().count() + 1) + str(self.name))
		super(Tag, self).save(*args, **kwargs)

	def isValidTag(self):
		return len(self.name) > 0

	def __format__(self):
		return f"{self.id} {self.name} ({self.domain})"
	
	class Meta:
		ordering = ['id']

	def __str__(self):
		return f"{self.id}. {self.name}"


class Article(models.Model):

	title = models.CharField(validators=[MinLengthValidator(1)], max_length=64, blank=False, null=False, default="Article")

	description = models.TextField(max_length=800, blank=False, null=False, default="Describe the article...")

	image = models.ImageField(upload_to="images/articles", blank=False, null=False)

	price = models.DecimalField(decimal_places=4, max_digits=9, validators=[MinValueValidator(1)], blank=False, null=False)

	tags = models.ManyToManyField(Tag, blank=True, related_name="tags")

	pub_ts = models.DateTimeField(auto_now_add=True)
	updated_ts = models.DateTimeField(auto_now=True)

	slug = models.SlugField(max_length=64, blank=False, null=False, unique=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(str(Article.objects.all().count() + 1) + str(self.title))
		super(Article, self).save(*args, **kwargs)

	def isValidArticle(self):
		return (len(self.title) > 0 and self.price > 0)

	def __format__(self):
		return f"{self.id}"

	class Meta:
		ordering = ['id']

	def __str__(self):
		return f"{self.id}. {self.title} {self.price}"


class Person(models.Model):

	options = (('M', 'Male'), ('F', 'Female'), ('X', 'Not Preferred to say'))

	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="person")
	profile = models.ImageField(upload_to="images/persons", blank=True, null=False)

	username = models.CharField(max_length=64, blank=False, null=False, unique=True)
	bio = models.TextField(max_length=500, blank=True, null=False)

	first = models.CharField(max_length=64, blank=False, null=False)
	last = models.CharField(max_length=64, blank=True, null=False)

	age = models.IntegerField(validators=[MinValueValidator(1)], blank=False, null=False, default=1)
	sex = models.CharField(max_length=1, choices=options, blank=False, null=False, default='X')
	
	email = models.EmailField(blank=False, null=False, unique=True)
	ph_no = models.BigIntegerField(blank=False, null=False, unique=True)

	tags = models.ManyToManyField(Tag, blank=True, related_name="ptags")

	retreated = models.ManyToManyField(Article, blank=True, related_name="retreated")

	rented = models.ManyToManyField(Article, blank=True, related_name="rented")
	purchased = models.ManyToManyField(Article, blank=True, related_name="purchased")

	sold = models.ManyToManyField(Article, blank=True, related_name="sold")
	display = models.ManyToManyField(Article, blank=True, related_name="display")

	bookmarked = models.ManyToManyField(Article, blank=True, related_name="bookmarked")
	carted = models.ManyToManyField(Article, blank=True, related_name="carted")

	friends = models.ManyToManyField('self', blank=True, related_name="friends")

	allowsMessage = models.BooleanField(blank=False, null=False, default=True)

	created_ts = models.DateTimeField(auto_now_add=True)
	updated_ts = models.DateTimeField(auto_now=True)

	slug = models.SlugField(max_length=64, blank=False, null=False, unique=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(str(Person.objects.all().count() + 1) + str(self.first) + ' ' + str(self.last))
		super(Person, self).save(*args, **kwargs)

	def isDisplayed(self):
		return self.display.all().count() > 0

	def isValidPerson(self):
		return (self.id > 0 and len(self.first + self.last) > 0)
	
	def __format__(self):
		return f"{self.id}"

	class Meta:
		ordering = ['id']

	def __str__(self):
		return f"{self.id}. {self.first} {self.last}  {self.age}"


class Message(models.Model):

	sender = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="sender", default=1)
	receiver = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="receiver", default=1)

	text = models.TextField(max_length=255, blank=False, null=False)

	timestamp = models.DateTimeField(auto_now_add=True)

	slug = models.SlugField(max_length=64, blank=False, null=False, unique=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(str(Message.objects.all().count() + 1))
		super(Message, self).save(*args, **kwargs)

	def isValidMessage(self):
		return len(self.text) > 0 and (self.sender.isValidPerson() and self.receiver.isValidPerson())

	def __format__(self):
		return f"{self.id}"

	class Meta:
		ordering = ['timestamp']

	def __str__(self):
		return f"{self.id}. {self.text} {self.timestamp}"


class Chat(models.Model):
	
	left =  models.ForeignKey(Person, on_delete=models.CASCADE, related_name="left", default=1)
	right = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="right", default=1)

	messages = models.ManyToManyField(Message, blank=True, related_name="messages")

	created_ts = models.DateTimeField(auto_now_add=True)
	updated_ts = models.DateTimeField(auto_now=True)
	
	slug = models.SlugField(max_length=64, blank=False, null=False, unique=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(str(Chat.objects.all().count() + 1))
		super(Chat, self).save(*args, **kwargs)

	def isValidChat(self):
		return (self.left.isValidPerson() and self.right.isValidPerson())
	
	def __format__(self):
		return f"{self.id}"

	class Meta:
		ordering = ['id']

	def __str__(self):
		return f"{self.id}. ({self.left.first} {self.left.last} <-> {self.right.first} {self.right.last})"


