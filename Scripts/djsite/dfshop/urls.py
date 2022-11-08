from django.urls import path

from . import views

urlpatterns = [
    path('goods/', views.goods, name='goods'),
    path('goods/<str:good>/good_details', views.good_details, name='good_details')
]