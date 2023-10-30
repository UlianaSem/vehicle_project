from datetime import datetime, timedelta

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from users.models import User
from vehicle.models import Moto, Car


@shared_task
def check_milage(pk, vehicle):
    if vehicle == "Moto":
        instance = Moto.objects.get(pk=pk)

    else:
        instance = Car.objects.get(pk=pk)

    if instance:
        prev_milage = -1

        for m in instance.milage.all():
            if prev_milage == -1:
                prev_milage = m.distance

            if prev_milage < m.distance:
                print("Wrong milage")
                break


@shared_task
def check_filter():
    filter_item = {"price__lte": 500}

    date = datetime.utcnow().date() - timedelta(days=30.5)

    users = [user.email for user in User.objects.filter(last_login__lte=date)]

    if Car.objects.filter(**filter_item).exist():
        send_mail(
            subject="Есть машина под ваш запрос",
            message="Заходите на наш сайт! Есть машина под ваш запрос.",
            recipient_list=users,
            from_email=settings.EMAIL_HOST_USER,
            fail_silently=False
        )
