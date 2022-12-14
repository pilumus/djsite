from django.urls import path, include

from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = "dfshop"

urlpatterns = [
    path('goods/', views.goods, name='goods'),
    path('goods/<str:good>/good_details', views.good_details,
         name='good_details'),
    path('', views.indexView, name='home'),
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('login/', LoginView.as_view(next_page='dfshop:dashboard'),
         name='login_url'),
    path('register/', views.registerView, name='register_url'),
    # path('logout/', LogoutView.as_view(next_page='dfshop:dashboard'),
    #      name='logout'), #name = logout

    # path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('cart/', views.cartView, name='cart'),
]