from django.db import models
from django.db.models.fields import CharField
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator

from django.contrib.auth.models import User

from datetime import datetime

# Create your models here.

class Article(models.Model):

    name = models.CharField(max_length=64, blank=False, null=False)

    description = models.CharField(max_length=255, blank=True, null=False)

    image = models.ImageField(blank=True, null=False)

    price = models.FloatField(validators=[MinValueValidator(1)], blank=False, null=False)

    # sold = models
    def __str__(self):
        return f"{self.name}"
     
    # class Meta:
    #     proxy = True


class Person(models.Model):

    options = (('M', 'Male'), ('F', 'Female'), ('X', 'Not Preferred to say'))

    id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")

    first = models.CharField(max_length=64, blank=False, null=False)
    last = models.CharField(max_length=64, blank=True, null=False)

    age = models.IntegerField(blank=False, null=False)
    sex = models.CharField(max_length=1, choices=options, blank=False, null=False, default='X')
    email = models.EmailField(blank=False, null=False)
    ph_no = models.BigIntegerField(blank=False, null=False)

    bought = models.ManyToManyField(Article, related_name="purchased")
    rented = models.ManyToManyField(Article)
    sold = models.ManyToManyField(Article, related_name="")

    bookmarked = models.ManyToManyField(Article)

    def __str__(self):
        return f"{self.first} {self.last}  {self.age}  {self.sex}"

class Message(models.Model):

    sender = models.ForeignKey(Person)
    receiver = models.ForeignKey(Person)

    text = models.CharField(min_length=1, max_length=255, blank=True, null=False)

    timestamp = models.DateTimeField(blank=False, null=False, default=datetime.now)

    
