from django.contrib import admin
from .models import FeedElement, SearchTag, ImageTags
admin.site.register(FeedElement)
admin.site.register(SearchTag)
admin.site.register(ImageTags)
# Register your models here.
