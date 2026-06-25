
from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home,name="Home page"),
    path('posts/<int:id>/',views.dynamic_view,name="dynamic page"),
    
]
