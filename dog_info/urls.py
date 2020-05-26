from django.urls import path
from . import views

urlpatterns = [
    path('api/dog/', views.DogListCreate.as_view()),
]