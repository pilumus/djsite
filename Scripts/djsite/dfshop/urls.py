from django.urls import path

from . import views

urlpatterns = [
    path('goods/', views.goods, name='goods'),
]