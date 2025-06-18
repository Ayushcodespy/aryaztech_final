from django.shortcuts import render
from main.models import Contact

# Create your views here.

from urllib import request
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage

from .forms import contactFormValidate
from django.contrib import messages

def homePage(request):
    return render(request,"home.html")

def aboutPage(request):
    return render(request,"aboutus.html")

def servicePage(request):
    return render(request,"services.html")

def careersPage(request):
    return render(request,"careers.html")

def contactPage(request):
    return render(request,"contact.html")

def sendMail(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        validation = contactFormValidate(name, email, message)
        if validation == True:
            try:
                contact = Contact(name=name, email=email, message=message)
                contact.save()

                html_content = render_to_string('email_template.html', {
                    'name': name,
                })

                email_message = EmailMessage(
                    "",
                    html_content,
                    "aryaztech01@gmail.com",  # From email address
                    [email],  # To email address
                )

                email_message.content_subtype = "html"  # Mark the content as HTML

                # Optionally, you can attach an image or file
                # email_message.attach_file('static\media\logo.png')

                # Send the email
                email_message.send(fail_silently=False)

                messages.success(request, "Message sent successfully!")

            except Exception as e:
                messages.error(request, "There was an error sending your message. Please try again later.")

        else:
            messages.error(request, validation)    
            return redirect('contact')

    return render(request, "contact.html")

