from django.shortcuts import render
from app.models import Contact, Portfolio
from .emails import contact_message

# Create your views here.

def home(request):
    items = Portfolio.objects.all()
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        recipient = 'njerimwanjiku@gmail.com'
        contact_message('njerimwanjiku@gmail.com', 'njerimwanjiku@gmail.com')


        new_message = Contact.objects.create(email=email, subject=subject,message=message)
        new_message.save()


        return render(request, 'success.html' )
    return render(request, 'index.html', {'items': items})

