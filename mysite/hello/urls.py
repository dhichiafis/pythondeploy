from django.urls import path
from . import views

app_name='hello'
urlpatterns=[
    path('goodbye/',views.goodbye,name='goodbye'),
    path('hello/',views.hello,name='hello')
]