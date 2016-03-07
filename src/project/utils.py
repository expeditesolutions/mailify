from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_templated_email(subject, to, txt_template, html_template, context):
    """
    Sends an email to an address with given subject, txt_template,
    html_template & context.
    """
    msg = EmailMultiAlternatives(
        subject,
        render_to_string(txt_template, context),
        settings.DEFAULT_FROM_EMAIL,
        [to])
    msg.attach_alternative(render_to_string(html_template, context), 'text/html')
    return msg.send()
