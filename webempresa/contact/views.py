from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.

def contact(request):
    #print("Tipo de peticion: {}".format(request.method))
    contact_form = ContactForm()

    if request.method == 'POST': 
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #enviamos correo y redireccionamos 
            email = EmailMessage(
                'La Caffeteria: Nuevo Mensaje de contacto', 
                'De {} <{}>\n\nEscribio:\n\n{}'.format(name, email, content),
                'No-contestar@inbox.mailtrap.io',
                ['sergioev@gmail.com'],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+'?ok')
            except:
                #algo no ha ido bien redireccionamos a fail 
                return redirect(reverse('contact')+'?fail')



    return render(request, 'contact/contact.html', {'form': contact_form}) 
