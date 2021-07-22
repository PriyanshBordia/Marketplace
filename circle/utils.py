import os
import time

from termcolor import cprint

def set_unique_name(image, pub_ts):
	image_name = 'Image_' + pub_ts.strftime("%Y-%m-%d_at_%H.%M.%S")
	image = '../staticfiles/' + str(image)
	cprint(image, 'cyan')
	os.rename(image, 'static/media/images/' + str(image_name) + '.png')
