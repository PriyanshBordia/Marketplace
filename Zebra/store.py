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
