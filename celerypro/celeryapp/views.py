from django.shortcuts import render,HttpResponse
# Create your views here.sleepy
from .task import sendgrid_mail,print_task
from sendgrid.helpers.mail import To
# 'd-37a7ab3963d945f48a64c89a52f56de3'
# {'name':'vrutti'}
# TO_EMAILS = [
#     To(
#         email='saloni.citrusbug@gmail.com',  # update with your email
#         substitutions={
#             'name': 'James',
#         }
#     )
# ]
def index(request):
    # sleepy.delay(4)
    # sendgrid_mail.delay(to_email=['saloni.citrusbug@gmail.com','abca@yopmail.com'],TEMPLATE_KEY='d-37a7ab3963d945f48a64c89a52f56de3',dynamic_data_for_template={'name':'vrutti'})
    print_task.delay()
    # sendgrid_mail.delay(to_email='saloni.citrusbug@gmail.com',TEMPLATE_KEY='d-37a7ab3963d945f48a64c89a52f56de3', dynamic_data_for_template={'name':'vrutti'})
    return HttpResponse("dfjhsdgf")