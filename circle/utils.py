import os
from datetime import datetime

from termcolor import cprint

def set_unique_name(image, pub_ts):
	img_dir = 'static/media/images/persons/'
	image_name = 'Image_' + pub_ts.strftime("%Y-%m-%d_at_%H.%M.%S") + '.png'
	image = img_dir + str(image)
	os.rename(img_dir + image,  str(image_name))
