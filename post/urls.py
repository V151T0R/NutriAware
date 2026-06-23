
from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.static_view,name="Home page"),
    path('home/posts/<int:id>/',views.dynamic_view,name="dynamic page")
]
