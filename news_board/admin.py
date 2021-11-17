from django.contrib import admin
from .models import News, Comments, Meta

# Register your models here.

admin.site.register(News)
admin.site.register(Comments)
admin.site.register(Meta)
