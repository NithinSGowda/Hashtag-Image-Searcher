from django.urls import path
from home import views
 
urlpatterns = [
    path('', views.home_feed, name="home_feed"),
    path('hsearch',views.hsearch,name='hsearch'),
    path('apidoc',views.api_doc),
	path('api/', views.api),
    path('update_db',views.update_db,name='update_db'),
    
]