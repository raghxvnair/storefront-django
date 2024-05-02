from django.urls import path
from . import views

app_name = 'playground'
#URL COnfig
urlpatterns = [
    path('hello/', views.say_hello, name='hello')
]