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
