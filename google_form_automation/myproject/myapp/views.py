from django.shortcuts import render

# Create your views here.
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings  # Importing the settings module
import os


def send_email(request):
    subject = 'Python (Selenium) Assignment - Shubham Sharma'
    body = ('Please find the screenshot of the filled form attached below as mentioned in the assignment for the '
            'application of internship')
    from_email = settings.EMAIL_HOST_USER
    to_email = ['tech@themedius.ai']
    cc_email = ['HR@themedius.ai', 'shubham160r@gmail.com']     # cc to myself in order to check

    email = EmailMessage(subject, body, from_email, to_email, cc=cc_email)

    base_dir = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__)))
    image_path = os.path.join(base_dir, 'confirmation_page.png')

    try:
        with open(image_path, 'rb') as f:
            email.attach('confirmation_page.png', f.read(), 'image/png')
    except FileNotFoundError:
        return HttpResponse('Image file not found.', status=404)

    email.send()

    return HttpResponse('Email sent successfully!')