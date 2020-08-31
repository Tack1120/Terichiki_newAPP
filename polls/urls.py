from django.urls import path
from .views import VerbListView
from . import views

urlpatterns = [
    path('', views.textform, name='textform')
]