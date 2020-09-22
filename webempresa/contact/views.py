from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm


def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #Enviamos el correo y redireccionamos
            email = EmailMessage(
                "La cafetera: Nuevo mensaje de contacto",
                "De {} <{}>\n\n Escribio:\n\n {}".format(name,email,contact),
                "no-contestar@inbox.mailtrap.io",
                ["pao.paotorres18@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                #Algo ha ido bien, redireccionamos
                return redirect(reverse('contact')+"?ok")
            except:
                #Algo no ha ido bien
                return redirect(reverse('contact')+"?fail")
    
    return render(request, "contact/contact.html",{'form':contact_form})