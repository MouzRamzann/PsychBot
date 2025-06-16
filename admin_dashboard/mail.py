from django.core.mail import send_mail
from chatbot import settings


# @csrf_exempt
def send_email(email, value):
    try:
        if value == 'approved':
            subject = 'Thank you for applying as a Doctor.'
            message = 'We are please to inform you that your request has been accepted. ' \
                      'Our admin will get back to you regarding further information about your profile and availability.'
            email_address = email
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email_address]
            send_mail(subject, message, email_from, recipient_list)
            return True
        else:
            subject = 'Thank you for applying as a Doctor.'
            message = 'We are sorry to inform you that we may not be proceeding with your application as your profile does not match our basic criteria.'
            email_address = email
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email_address]
            send_mail(subject, message, email_from, recipient_list)
            return True
    except Exception as e:
        print(e)
        return False
