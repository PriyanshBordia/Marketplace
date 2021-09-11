import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def set_unique_name(image, pub_ts):
	img_dir = '/circle/static/media/images/persons/' # Path from BASE_DIR
	image_name = 'Image_' + pub_ts.strftime("%Y-%m-%d_at_%H.%M.%S") + '.png'
	os.rename(img_dir + image,  str(image_name))


def send_mail(client, recipient, sender, subject, message):

	msg = MIMEMultipart()
	msg['From'] = sender
	msg['To'] = recipient
	msg['Subject'] = subject
	msg.attach(MIMEText(message))

	mail_server = "django.core.mail.backends.smtp.EmailBackend"
	mail_port = os.environ.get('EMAIL_HOST_PORT')
	mail_username = os.environ.get('EMAIL_HOST_USERNAME')
	mail_password = os.environ.get('EMAIL_HOST_PASSWORD')

	server = smtplib.SMTP(mail_server, mail_port)
	server.starttls()
	server.login(mail_username, mail_password)
	server.sendmail(sender, recipient, msg.as_string())
	server.quit()
