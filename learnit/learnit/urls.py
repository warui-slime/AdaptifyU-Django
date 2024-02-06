
from django.contrib import admin
from django.urls import path,include
from users import views as user_views
from django.contrib.auth import views as auth_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include("allauth.urls")),
    path('',include('home.urls')),
    path('register',user_views.register,name='register'),
    path('login/',auth_user.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',user_views.logout_user,name='logout'),
]
