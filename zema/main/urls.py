from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('test', views.test, name='test'),
    path('data', views.data, name='data'),
    path('article', views.article, name='article'),
]