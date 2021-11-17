from .models import News


def my_scheduled_job():
    news = News.objects.all()
    for item in news:
        item.amount_of_upvotes = 0
        item.save()
