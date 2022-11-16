from celery import shared_task
from time import sleep
# from django.core.mail import send_mail
from django.shortcuts import HttpResponse
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Email, Mail, Personalization
from python_http_client import exceptions
from django.conf import settings
# TEMPLATE_KEY='d-37a7ab3963d945f48a64c89a52f56de3'
# TO_EMAILS = ['saloni.citrusbug@gmail.com','abca@yopmail.com']
@shared_task
def sleepy(duration):
    sleep(duration)
    return None
    
@shared_task
def sendgrid_mail():

    try:
        message = Mail(from_email=settings.SENDGRID_FROM_MAIL,
                        to_emails=['abca@yopmail.com','a@yopmail.com'],
                        subject="ghasdfghasdf",
                        html_content="csdgjhd")
        message.dynamic_template_data={'name':'vrutti'}
        message.template_id='d-37a7ab3963d945f48a64c89a52f56de3'
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.body, ";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        print("____________________________________________________________________________")
        print(response.status_code)
        print("____________________________________________________________________________")

        print(response.body)
        print("____________________________________________________________________________")

        print(response.headers)
        print("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")

        return HttpResponse("fvhfsdfvbhfb")
        # return response
    except exceptions.BadRequestsError as e:
        print("sendgrid error-",e.body)
        pass