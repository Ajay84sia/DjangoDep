from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path("", views.welcome, name="welcome"),
    path("greet/<str:username>/", views.greet, name="greet"),
    path("farewell/<str:username>/", views.farewell, name="farewell"),
]