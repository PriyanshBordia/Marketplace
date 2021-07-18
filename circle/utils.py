import os
import time

def get_image_name(self, pub_ts):
	self.image_name = 'Image_' + pub_ts.strftime("%Y-%m-%d_at_%H.%M.%S")
