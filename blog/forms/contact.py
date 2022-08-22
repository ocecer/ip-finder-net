from django.core.mail import send_mail
from django import forms
from blog.models import ContactModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ('fullName', 'email', 'message')

    def send_email(self, message):
        send_mail(
            subject='There is a new Message from contact form!',
            message=message,
            from_email=None,
            recipient_list=['omercanecer@gmail.com'],
            fail_silently=False
        )
