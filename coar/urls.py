from .views import home,info, search_info
from django.urls import path

urlpatterns = [
    path('', home,name="home"),
    path("info/", info,name="info"),
    path("search_info/", search_info,name="search_info")

    
]
