from django.template.defaulttags import url
from django.urls import path
from . import views


app_name = 'catalog'
urlpatterns = [
    path('', views.index, name='index'),
    url(r'^books/$', views.models.BookListViews.as_view(), name='books'),
]
