from django.conf.urls import url, include
from django.urls import path
from .views import *
from .def_date import *

urlpatterns = [
    path('', date_page, name = 'date_url')
]
