from .models import Meta
import time

try:
    date = Meta.objects.get(pk=1)
except:
    date = Meta(day=time.strftime("%x"))
    date.save()