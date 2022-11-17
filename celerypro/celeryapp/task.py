from celery import shared_task
from time import sleep
# from django.core.mail import send_mail
from django.shortcuts import HttpResponse
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Email, Mail, Personalization,To
from python_http_client import exceptions
from django.conf import settings
# TEMPLATE_KEY='d-37a7ab3963d945f48a64c89a52f56de3'
# TO_EMAILS = ['saloni.citrusbug@gmail.com','abca@yopmail.com']
# @shared_task
# def sleepy(duration):
#     sleep(duration)
#     return None
    # from_email=settings.SENDGRID_FROM_MAIL,
    #                     to_emails=to_email,
    #                     subject="ghasdfghasdf",
    #                     html_content="csdgjhd"
@shared_task
def print_task():
    print("heeelllloooooz")



@shared_task
def sendgrid_mail(to_email,TEMPLATE_KEY, dynamic_data_for_template):

    try:
        message = Mail()
        message.template_id=TEMPLATE_KEY
        message.from_email = Email(settings.SENDGRID_FROM_MAIL)
        message.dynamic_template_data=dynamic_data_for_template
        message.template_id=TEMPLATE_KEY
        p=Personalization()
        p.add_to(Email(to_email))
        p.dynamic_template_data = dynamic_data_for_template
        message.add_personalization(p)
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

        return "DONE"
        # return response
    except exceptions.BadRequestsError as e:
        print("sendgrid error-",e.body)
        pass