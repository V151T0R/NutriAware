
from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home,name="home"),
    path('post_<int:id>/',views.dynamic_view,name="dynamic_view"),
    
]
