from django.shortcuts import render
from django.views import View
from .models import News, Meta
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NewsSerializer, CommentsSerializer
import time
from .cron import my_scheduled_job

# Create your views here.


class Index(View):
    def get(self, request):
        self.news = News.objects.all()
        self.context = {
            "news": self.news,
        }
        return render(request, "news_board/index.html", self.context)


@api_view(["GET"])
def read_news(request):
    date = Meta.objects.get(pk=1)
    if date.day != time.strftime("%x"):
        my_scheduled_job()
        date.day = time.strftime("%x")
        date.save()
    news = News.objects.all()
    serializer = NewsSerializer(news, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def detail_news(request, pk):
    news = News.objects.get(id=pk)
    serializer = NewsSerializer(news, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def create_news(request):
    serializer = NewsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
def update_news(request, pk):
    news = News.objects.get(id=pk)
    serializer = NewsSerializer(instance=news, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_news(request, pk):
    news = News.objects.get(id=pk)
    news.delete()
    return Response("Deleted")


# =====


@api_view(["GET"])
def read_comments(request, pk):
    news = News.objects.get(id=pk)
    comments = news.comments_set.all()
    serializer = CommentsSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def read_one_comment(request, pk, id):
    news = News.objects.get(id=pk)
    comment = news.comments_set.get(id=id)
    serializer = CommentsSerializer(comment, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def create_comment(request, pk):
    serializer = CommentsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
def update_comment(request, pk, id):
    news = News.objects.get(id=pk)
    comment = news.comments_set.get(id=id)
    serializer = CommentsSerializer(instance=comment, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_comment(request, pk, id):
    news = News.objects.get(id=pk)
    comment = news.comments_set.get(id=id)
    comment.delete()
    return Response("Deleted")


# ===


@api_view(["GET"])
def upvote(request, pk):
    request.session.set_expiry(86400)  # 24 hours
    news = News.objects.get(id=pk)
    request.session["upvoted"] = request.session.get(
        "upvoted",
        [
            "None",
        ],
    )
    if news.title in request.session["upvoted"]:
        serializer = NewsSerializer(news, many=False)
        return Response(serializer.data)
    elif request.session["upvoted"] != "None":
        request.session["upvoted"].append(news.title)
        news.amount_of_upvotes += 1
        news.save()
    else:
        request.session["upvoted"] = [
            news.title,
        ]
        news.amount_of_upvotes += 1
        news.save()
    serializer = NewsSerializer(news, many=False)
    return Response(serializer.data)
