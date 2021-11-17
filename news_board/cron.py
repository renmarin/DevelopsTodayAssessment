from .models import News


def my_scheduled_job():
    news = News.objects.values()
    for item in news:
        item["amount_of_upvotes"] = 0
        news.save()
