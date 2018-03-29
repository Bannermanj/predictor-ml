from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.ListTeam.as_view()),
    url('<int:pk>/', views.DetailTeam.as_view()),

]
