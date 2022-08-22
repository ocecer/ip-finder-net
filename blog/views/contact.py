from blog.forms import ContactForm
from django.views.generic import FormView


class ContactFormView(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = '/message-sent'

    def form_valid(self, form):
        form.save()
        form.send_email(message=form.cleaned_data.get('message'))
        return super().form_valid(form)
