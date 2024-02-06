from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_user



urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('login/',auth_user.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('pricing/',views.pricing,name = 'pricing'),
    path('dashboard/',views.dashboard,name = 'dashboard'),
    path('services/',views.services,name = 'services'),
]