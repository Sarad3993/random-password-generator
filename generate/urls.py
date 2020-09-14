from django.urls import path 
from generate.views import *

app_name = 'generate'

urlpatterns = [
    path('',password_generate,name='password_generate'),
]