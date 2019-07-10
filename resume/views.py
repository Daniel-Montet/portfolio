from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from . import forms
from . import models
# Create your views here.


def resume(request):

    projects = models.Project.objects.all()
    blogs = models.Blog.objects.all()
    resumes = models.ResumeHardCopy.objects.all()

    django = models.Project.objects.filter(framework='Django')
    angular = models.Project.objects.filter(framework='Angular7-FirebaseOAuth')
    flask = models.Project.objects.filter(framework='Flask')
    javascript = models.Project.objects.filter(framework='Javascript')


    if request.method == 'POST':
        form = forms.MailMe(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            sender = form.cleaned_data['email']
            message = form.cleaned_data['message']
            recipients = ['dmontetproff@gmail.com']

            send_mail(name, message, sender, recipients)
            messages.add_message(request, messages.SUCCESS, "Message Sent Successfully :)")

    else:
        form = forms.MailMe()

    return render(request, 'resume/index.html',
            {
                'form':form,
                'projects': projects,
                'blogs': blogs,
                'django': django,
                'angular': angular,
                'flask': flask,
                'javascript': javascript,

                })
