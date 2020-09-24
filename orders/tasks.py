from celery import task
from django.core.mail import send_mail

from .models import Order


@task
def order_created(order_id):
    # order = Order.objects.get(id=order_id)
    # subject = f"Order nr. {order.id}"
    # message = f"Dear {order.first_name} \n\nyou have successfully " \
    #           f"placed an order\n\nyour order id is {order.id}"
    # mail_sent = send_mail(subject, message, 'ahmedeid6422@gmail.com', [order.email])

    return "mail_sent"
