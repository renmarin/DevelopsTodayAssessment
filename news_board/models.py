from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    creation_date = models.DateTimeField()
    amount_of_upvotes = models.IntegerField(default=0)
    author_name = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Comments(models.Model):
    author_name = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    creation_date = models.DateTimeField()
    news_f = models.ForeignKey(News, on_delete=models.CASCADE)


class Meta(models.Model):
    day = models.CharField(max_length=50)
