from django.shortcuts import render, redirect
import requests
from .forms import Subscriberform, MailMassageForm
from .models import Subcriber, MailMessage
from django.contrib import messages
from django.core.mail import send_mail 
from django_pandas.io import read_frame
from django.conf import settings


def home(request):
    if request.method == 'POST':
        form = Subscriberform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription Successful')
            return redirect('/')
    else:
        form = Subscriberform()
    context = {
        'form':form,
    }
    return render(request, 'files/index.html', context)

def sendmail(request):
    emails = Subcriber.objects.all()
    df = read_frame(emails, fieldnames=['email'])
    mail_list = df['email'].values.tolist()
    print(mail_list)
    if request.method == 'POST':
        form = MailMassageForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            send_mail(
                title,
                message,
                '',
                mail_list,
                fail_silently=False,
            )
            messages.success(request, 'Message has been sent to the mail list')
            return redirect('mail')
    else:
        form = MailMassageForm()
    context = {
        'form':form
    }
    return render(request, 'files/sendmail.html', context)

