from django.shortcuts import render
from ContactsApp.models import Contact,PhoneNumber
from ContactsApp.forms import PhoneNumberForm, ContactForm
from django.shortcuts import redirect

#creating the landing page
def index(request):
    contact_list = Contact.objects.all()
    context = {'contact_list': contact_list }
    return render(request, 'ContactsApp/contacts.html', context)


def get_contact_details(request):
    if request.method == 'GET':
        try:
            contact = Contact.objects.get(id=request.GET.get('contact_id'))
            context = {'contact': contact }
            return render(request, 'ContactsApp/contact.html', context)
        except:
            return render(request, 'ContactsApp/error.html')



def add_new_number(request):
    if request.method == 'POST':
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('./')
    if request.method == 'GET':
        try:
            numberForm = PhoneNumberForm( initial= {'contact_id': request.GET.get('contact_id')})
            return render(request, 'ContactsApp/create_number.html', {'form': numberForm})
        except Exception as e:
            return render(request, 'ContactsApp/error.html')



def create_new_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('./')
    if request.method == 'GET':
        try:
            contactForm = ContactForm()
            return render(request, 'ContactsApp/create_contact.html', {'form': contactForm})
        except Exception as e:
            return render(request, 'ContactsApp/error.html')


