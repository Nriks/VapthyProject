from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
# Create your views here.
from .forms import ContactForm


def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['vapthy@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact/formContact.html", {'form': form})

    # form_class = ContactForm
    # # if request is not post, initialize an empty form
    # form = form_class(request.POST or None)
    # if request.method == 'POST':

    #     if form.is_valid():
    #         nome = request.POST.get('nome')
    #         email = request.POST.get('email')
    #         msg = request.POST.get('msg')

    #         send_mail('Subject here', msg, email, ['testmail@gmail.com'], fail_silently=False)
    #         return HttpResponseRedirect('blog/inicio')
    # return render(request, 'blog/inicio.html', {'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')
