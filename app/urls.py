from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('admin/', admin.site.urls),
    path('ss/', views.ss),
    path('api/', views.api),
    path('hsearch',views.hsearch,name='hsearch')
]
