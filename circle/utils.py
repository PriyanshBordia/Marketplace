import os

def set_unique_name(image, pub_ts):
	img_dir = '/circle/static/media/images/persons/' # Path from BASE_DIR
	image_name = 'Image_' + pub_ts.strftime("%Y-%m-%d_at_%H.%M.%S") + '.png'
	os.rename(img_dir + image,  str(image_name))
