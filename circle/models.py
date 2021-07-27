from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MinLengthValidator

from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):

	name = models.CharField(max_length=64, blank=False, null=False)

	domain = models.CharField(max_length=64, blank=False, null=False, default="General")

	description = models.TextField(max_length=511, blank=False, null=False, default="A Tag")

	# created_ts = models.DateTimeField(auto_now_add=True)
	# updated_ts = models.DateTimeField(auto_now=True)

	slug = models.SlugField(max_length=64, blank=False, null=False, unique=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Tag, self).save(*args, **kwargs)

	def isValidTag(self):
		return len(self.name) > 0

	def __format__(self):
		return f"{self.id} {self.slug}"
	
	class Meta:
		ordering = ['id']

	def __str__(self):
		return f"{self.name}"


class Article(models.Model):

	title = models.CharField(validators=[MinLengthValidator(1)], max_length=64, blank=False, null=False, default="Article")

	description = models.TextField(max_length=255, blank=False, null=False, default="Describe the article...")

	image = models.ImageField(upload_to="images/articles", blank=False, null=False)

	price = models.FloatField(validators=[MinValueValidator(1)], blank=False, null=False)

	tags = models.ManyToManyField(Tag, blank=True, related_name="tags")

	pub_ts = models.DateTimeField(auto_now_add=True)
	# updated_ts = models.DateTimeField(auto_now=True)

	slug = models.SlugField(max_length=64, blank=False, null=False, unique=True)


	def save(self, *args, **kwargs):
		self.slug = slugify(self.title + str(self.id) + str(self.pub_ts) + str(self.price))
		super(Article, self).save(*args, **kwargs)

	def isValidArticle(self):
		return len(self.title) > 0 and self.price > 0

	def __format__(self):
		return f"{self.id} {self.slug}"

	class Meta:
		ordering = ['id']

	def __str__(self):
		return f"{self.title} {self.price}"


class Person(models.Model):

	options = (('M', 'Male'), ('F', 'Female'), ('X', 'Not Preferred to say'))

	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
	profile = models.ImageField(upload_to="images/persons", blank=True, null=False)

	username = models.CharField(max_length=64, blank=False, null=False, unique=True)
	bio = models.TextField(max_length=500, blank=True, null=False)

	first = models.CharField(max_length=64, blank=False, null=False)
	last = models.CharField(max_length=64, blank=True, null=False)

	age = models.IntegerField(validators=[MinValueValidator(1)], blank=False, null=False, default=1)
	sex = models.CharField(max_length=1, choices=options, blank=False, null=False, default='X')
	
	email = models.EmailField(blank=False, null=False, unique=True)
	ph_no = models.BigIntegerField(blank=False, null=False, unique=True)


	rented = models.ManyToManyField(Article, blank=True, related_name="rented")
	purchased = models.ManyToManyField(Article, blank=True, related_name="purchased")

	sold = models.ManyToManyField(Article, blank=True, related_name="sold")
	display = models.ManyToManyField(Article, blank=True, related_name="display")

	bookmarked = models.ManyToManyField(Article, blank=True, related_name="bookmarked")
	carted = models.ManyToManyField(Article, blank=True, related_name="carted")

	friends = models.ManyToManyField('self', blank=True, related_name="friends")

	allowsMessage = models.BooleanField(blank=False, null=False, default=True)

	# created_ts = models.DateTimeField(auto_now_add=True)
	# updated_ts = models.DateTimeField(auto_now=True)

	slug = models.SlugField(max_length=64, blank=False, null=False, unique=True)


	def save(self, *args, **kwargs):
		self.slug = slugify(self.username)
		super(Person, self).save(*args, **kwargs)

	def isValidPerson(self):
		return self.rented != self.sold
	
	def __format__(self):
		return f"{self.id} {self.slug}"

	class Meta:
		ordering = ['id']

	def __str__(self):
		return f"{self.first} {self.last}  {self.age}"


class Message(models.Model):

	text = models.TextField(max_length=255, blank=False, null=False, default="Type a Message...")

	timestamp = models.DateTimeField(auto_now_add=True)
	
	# created_ts = models.DateTimeField(auto_now_add=True)
	# updated_ts = models.DateTimeField(auto_now=True)

	slug = models.SlugField(max_length=64, blank=False, null=False, unique=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(str(self.text) + str(self.timestamp) + str(self.id))
		super(Message, self).save(*args, **kwargs)

	def isValidMessage(self):
		return len(self.text) > 0

	def __format__(self):
		return f"{self.id} {self.slug}"

	class Meta:
		ordering = ['timestamp']

	def __str__(self):
		return f"{self.text} {self.timestamp}"


class Chat(models.Model):
	
	sender = models.OneToOneField(Person, on_delete=models.CASCADE, related_name="sender")
	receiver = models.OneToOneField(Person, on_delete=models.CASCADE, related_name="receiver")

	messages = models.ManyToManyField(Message, blank=True, related_name="messages")

	created_date = models.DateTimeField(auto_now_add=True)

	# created_ts = models.DateTimeField(auto_now_add=True)
	# updated_ts = models.DateTimeField(auto_now=True)
	
	slug = models.SlugField(max_length=64, blank=False, null=False, unique=True)


	def save(self, *args, **kwargs):
		self.slug = slugify(str(self.sender) + str(self.receiver))
		super(Chat, self).save(*args, **kwargs)

	def isValidChat(self):
		return len(self.messages) >= 0 and (self.sender > 0) and (self.receiver > 0)
	
	def __format__(self):
		return f"{self.id} {self.slug}"

	class Meta:
		ordering = ['id']

	def __str__(self):
		return f"{self.sender.first} {self.sender.last} <-> {self.receiver.first} {self.receiver.last}"


# class Friend(models.Model):

# 	chat = models.ForeignKey(Chat, )
# 	created_ts = models.DateTimeField(auto_now_add=True)
# 	updated_ts = models.DateTimeField(auto_now=True)

# 	slug = models.SlugField(max_length=64, blank=False, null=False, unique=True)


# 	def save(self, *args, **kwargs):
# 		self.slug = slugify(self.username)
# 		super(Friend, self).save(*args, **kwargs)

# 	def isValidPerson(self):
# 		return self.rented != self.sold
	
# 	def __format__(self):
# 		return f"{self.id} {self.slug}"

# 	class Meta:
# 		ordering = ['id']

# 	def __str__(self):
# 		return f"{self.first} {self.last}  {self.age}  {self.sex}"


