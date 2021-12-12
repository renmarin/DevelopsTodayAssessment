from celery import shared_task

from .models import Meta, News
import time
from django.core.exceptions import ObjectDoesNotExist

import datetime

# reset upvotes every day
@shared_task
def reset_upvotes():
    # news = News(
    #     title='task',
    #     link='link',
    #     creation_date=datetime.datetime.now(),
    #     amount_of_upvotes='2',
    #     author_name='name')
    # news.save()
    try:
        date = Meta.objects.get(pk=1)
    except ObjectDoesNotExist:
        date = Meta(day=time.strftime("%x"))
        date.save()

    if date.day != time.strftime("%x"):
        news = News.objects.all()
        for item in news:
            item.amount_of_upvotes = 0
            item.save()
        date.day = time.strftime("%x")
        date.save()
