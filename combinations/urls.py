from django.urls import path
from combinations import views

urlpatterns = [
    path('combinations', views.get_combs, name='combinations'),
]