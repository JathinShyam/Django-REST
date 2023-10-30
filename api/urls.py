from home.views import index, person
from django.urls import path

urlpatterns = [
    path('index/', index, name='index'),
    path('person/', person, name='person'),
]