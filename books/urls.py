from django.urls import path

from . import views as v

app_name = 'books'
urlpatterns = [
    path('', v.IndexView.as_view(), name='index'),
    path('dispatch/', v.dispatch, name='dispatch'),
]
