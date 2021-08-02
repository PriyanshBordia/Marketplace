# try:
		# except KeyError:
			# return render(request, "circle/error.html", context={"message": "Upload file.!!", "type": "Key Error", "link": "newArticle"})
		# except ValueError:
			# return render(request, "circle/error.html", context={"message": "Invalid Value to given field image.!!", "type": "Value Error", "link": "newArticle"})
		# except TypeError:
			# return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "newArticle"})
			
# class Meta:
# 	db_table = "person"
# 	verbose_name = "Person"
# 	get_latest_by = "id"
# 	ordering = ['id']



# class Meta:
# 	# db_table = "person"
# 	verbose_name = "Messages"

# validators=[MinLengthValidator(1), MaxLengthValidator(255)],

# class Meta:
# 	db_table = 'article'
# 	verbose_name = 'circle_article'


# def login(request):
    # return render(request, "circle/home.html", context={})


# def logout(request):
    # return render(request, "circle/home.html", context={})


MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
}


def verification(request):

	ph_no = 9316300064
	request.session['ph_no'] = ph_no

	otp = str(random.randint(100000, 999999))

	cprint(otp, 'white')

	connection = http.client.HTTPSConnection("api.msg91.com")

	authkey = settings.authkey

	code = 91
	sender = "Marketplace Team"
	# payload = "{\"Value1\":\"Param1\",\"Value2\":\"Param2\",\"Value3\":\"Param3\"}"

	headers = {'content-type': "application/json"}

	connection.request("GET", "http://control.msg91.com/api/sendotp.php", params={
	                   "otp": otp, "mobile": ph_no, "sender": sender, "message": message, "country": code, "authkey": authkey, "otp_length": 6}, headers=headers)

	res = connection.getresponse()
	data = res.read()

	print(data)

	print(data.decode("utf-8"))

	return render(request, "circle/test.html", context={"message": "OTP sent.!!"})


	if request.GET:
		return HttpResponseRedirect(reverse('newArticle', args=()))
	else:
		user_id = request.user.id

		try:
			title = str(request.POST.get("title"))
		except KeyError:
			return render(request, "circle/error.html", context={"message": "Enter title.!!", "type": "Key Error", "link": "newArticle"})
		except ValueError:
			return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "newArticle"})
		except TypeError:
			return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "newArticle"})

		try:
			description =  str(request.POST.get('description'))
		except KeyError:
			return render(request, "circle/error.html", context={"message": "Enter description.!!", "type": "Key Error", "link": "newArticle"})
		except ValueError:
			return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "newArticle"})
		except TypeError:
			return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "newArticle"})

		try:
			price = float(request.POST.get('price'))
		except KeyError:
			return render(request, "circle/error.html", context={"message": "Enter price.!!", "type": "Key Error", "link": "newArticle"})
		except ValueError:
			return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "newArticle"})
		except TypeError:
			return render(request, "circle/error.html", context={"message": "Incompatible Tag DataType.!!", "type": "Type Error", "link": "newArticle"})

		# try:
		# 	tags = request.POST.get('tags')
		# 	if tags is not None:
		# 		tags = list(tags)
		# 	else:
		# 		tags = []
		# except KeyError:
		# 	return render(request, "circle/error.html", context={"message": "Enter title.!!", "type": "Key Error", "link": "newArticle"})
		# except ValueError:
		# 	return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "newArticle"})
		# except TypeError:
		# 	return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "newArticle"})

		image = request.FILES['image']

		article = Article.objects.create(title=title, description=description, image=image, price=price)
		# cprint(article, 'red')

		# pub_ts = article.pub_ts
		# cprint(pub_ts, 'white')

		# article.image = set_unique_name(article.image.url, pub_ts)
		# cprint(article.image.url, 'blue')

		# for tag in tags:
		# 	article.tags.add(tag)

		try:
			person = Person.objects.filter(user_id=user_id).first()
			person.display.add(article)
			person.save() 
			return HttpResponseRedirect(reverse("article", args=(article.id, )))
		except Person.DoesNotExist:  
			return render(request, "circle/error.html", context={"message": "No person found.!!", "type": "Data Error", "link": "newArticle"})

# if request.GET:
	# 	return HttpResponseRedirect(reverse('newPerson', args=()))
	# else:
		# try:
		# 	user = User.objects.get(pk=request.user.id)
		# 	try:
		# 		bio = str(request.POST.get("bio"))
		# 	except KeyError:
		# 		return render(request, "circle/error.html", context={"message":  "Enter a Bio.!!", "type": "Key Error", "link": "newPerson"})
		# 	except ValueError:
		# 		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "newPerson"})
		# 	except TypeError:
		# 		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "newPerson"})

		# 	try:
		# 		first = str(request.POST.get("first"))
		# 	except KeyError:
		# 		return render(request, "circle/error.html", context={"message":  "Enter a First Name.!!", "type": "Key Error", "link": "newPerson"})
		# 	except ValueError:
		# 		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "newPerson"})
		# 	except TypeError:
		# 		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "newPerson"})

		# 	try:
		# 		last = str(request.POST.get("last"))
		# 	except KeyError:
		# 		return render(request, "circle/error.html", context={"message":  "Enter a Last Name.!!", "type": "Key Error", "link": "newPerson"})
		# 	except ValueError:
		# 		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "newPerson"})
		# 	except TypeError:
		# 		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "newPerson"})

		# 	try:
		# 		age = int(request.POST.get("age"))
		# 	except KeyError:
		# 		return render(request, "circle/error.html", context={"message": "Enter a Age!", "type": "Key Error.!!", "link": "newPerson"})
		# 	except ValueError:
		# 		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "newPerson"})
		# 	except TypeError:
		# 		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "newPerson"})

		# 	try:
		# 		sex = str(request.POST.get("sex"))
		# 	except KeyError:
		# 		return render(request, "circle/error.html", context={"message": "Select gender from the options provided.!!", "type": "KeyError", "link": "newPerson"})
		# 	except ValueError:
		# 		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "newPerson"})
		# 	except TypeError:
		# 		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "newPerson"})

		# 	sex = sex[0]

		# 	try:
		# 		email = str(request.POST.get("email"))
		# 	except KeyError:
		# 		return render(request, "circle/error.html", context={"message": "Enter an e-mail address.!!", "type": "KeyError", "link": "newPerson"})
		# 	except ValueError:
		# 		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "newPerson"})
		# 	except TypeError:
		# 		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "newPerson"})

		# 	try:
		# 		ph_no = str(request.POST.get("ph_no"))
		# 	except KeyError:
		# 		return render(request, "circle/error.html", context={"message": "Enter an e-mail address.!!", "type": "KeyError", "link": "newPerson"})
		# 	except ValueError:
		# 		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "newPerson"})
		# 	except TypeError:
		# 		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "newPerson"})

		# 	username = email.split('@')[0]

		# 	profile = request.FILES['profile']

		# 	try:
		# 		Person.objects.create(user=user, profile=profile, username=username, bio=bio, first=first, last=last, age=age, sex=sex, email=email, ph_no=ph_no)
		# 		return HttpResponseRedirect(reverse('person', args=(person.id, )))
		# 	except:
		# 		return render(request, "circle/error.html", context={"message": "No person found.!!", "type": "Data Error", "link": "newPerson"})
		# except User.DoesNotExist:
		# 	return render(request, "circle/error.html", context={"message": "No user found.!!", "type": "Data Error", "link": "newPerson"})
