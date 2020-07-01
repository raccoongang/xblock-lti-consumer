"""
Defines asynchronous celery task for sending email notification (via EmailMultiAlternatives)
pertaining if a user got a grade in the LTI window, an email message sends for him
"""

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from xblockutils.resources import ResourceLoader

from lms import CELERY_APP


@CELERY_APP.task(name='lti_consumer.tasks.send_email_message')
def send_email_message(to_addr, subject, context):
    """
    Sends email with required context.

    :param to_addr: Email address of the student who earned grade.
    :param subject: Email subject of the student who earned grade.
    :param context: Context of the email message.
    """
    loader = ResourceLoader(__name__)

    text_content = loader.render_mako_template('/templates/email/user_score_notification.txt', context)
    html_content = loader.render_mako_template('/templates/email/user_score_notification.html', context)

    msg = EmailMultiAlternatives(subject, text_content, settings.DEFAULT_FROM_EMAIL, [to_addr])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
