from django.urls import path
from .views import Index
from . import views

app_name = "news_board"

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("api/read", views.read_news, name="read_all"),
    path("api/read/<str:pk>", views.detail_news, name="read"),
    path("api/update/<str:pk>", views.update_news, name="update"),
    path("api/delete/<str:pk>", views.delete_news, name="delete"),
    path("api/create", views.create_news, name="create"),
    path(
        "api/read/<str:pk>/comments",
        views.read_comments,
        name="read_commnets",
    ),
    path(
        "api/read/<str:pk>/comments/create",
        views.create_comment,
        name="create_commnet",
    ),
    path(
        "api/read/<str:pk>/comments/<str:id>",
        views.read_one_comment,
        name="read_one_commnet",
    ),
    path(
        "api/read/<str:pk>/comments/<str:id>/update",
        views.update_comment,
        name="update_commnet",
    ),
    path(
        "api/read/<str:pk>/comments/<str:id>/delete",
        views.delete_comment,
        name="delete_commnet",
    ),
    path("api/read/<str:pk>/upvote", views.upvote, name="upvote"),
]
