from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def send_mail(name, email):
    email_subject = 'Table Reservation'
    message = render_to_string('booking/reserved_email.html', {
        'name': name
    })
    email = EmailMessage(email_subject, message, to=[email])
    result = email.send()
    return result