from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^welcome/', views.welcome),
    url(r'^index/', views.index)
]