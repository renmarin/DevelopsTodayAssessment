from .models import Meta
import time
from django.core.exceptions import ObjectDoesNotExist

try:
    date = Meta.objects.get(pk=1)
except ObjectDoesNotExist:
    date = Meta(day=time.strftime("%x"))
    date.save()
