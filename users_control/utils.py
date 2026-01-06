from django.core.mail import send_mail
from django.conf import settings


def send_verification_email(user, code):
    verify_url = f"http://127.0.0.1:8000/users/verify/{code}"

    send_mail(
        subject="Email manzilingizni tasdiqlang",
        message=f"Havola: \n{verify_url}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False
    )