from django.shortcuts import render_to_response
from mysite.contact.forms import ContactForm
from django.http import HttpResponse

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_vaild():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email','noreply@example.com'),
                ['siteowner@example.com'],
                )
            return HttpResponseRedirect('/contact/thanks')
    else:
        form = ContactForm(initial={'subject':'have fun'})
    return render_to_response('contact_form.html',{'form':form})

def thanks(request):
    return HttpResponse("thanks for your visiting")
