
from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home,name="home"),
    path('post_<int:id>/',views.dynamic_view,name="dynamic_view"),
    path('create/', views.create_post, name='create_post'),
    path('delete/<int:id>/', views.delete_post, name='delete_post'),
]
