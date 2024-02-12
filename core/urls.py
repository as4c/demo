from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name= 'home-view'),
    path('write-article/', views.writeArticle, name= 'write-article')
]