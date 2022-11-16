from django.shortcuts import render,HttpResponse
# Create your views here.
from .task import sleepy,sendgrid_mail
# 'd-37a7ab3963d945f48a64c89a52f56de3'
# {'name':'vrutti'}
def index(request):
    sleepy.delay(4)
    # sendgrid_mail.delay(to_email=['saloni.citrusbug@gmail.com','abca@yopmail.com'],TEMPLATE_KEY='d-37a7ab3963d945f48a64c89a52f56de3',dynamic_data_for_template={'name':'vrutti'})
    sendgrid_mail.delay()
    return HttpResponse("dfjhsdgf")