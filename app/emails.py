from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string



def contact_message(email,receiver):
    # Creating message subject and sender
    subject = 'New Message Recieved!'
    sender = 'njerimwanjiku@gmail.com'

    #passing in the context vairables
    text_content = render_to_string('email/welcome.txt',{"email": email})
    html_content = render_to_string('email/welcome.html',{"email": email})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()