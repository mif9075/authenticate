from django.urls import path
from . import views

urlpatterns = [
    path('', views.es_home, name="es_home"),
    path('en/', views.en_home, name="en_home"),
    path('login/', views.es_login_user, name="es_login"),
    path('en/login/', views.en_login_user, name="en_login"),
    path('logout/', views.es_logout_user, name="es_logout"),
    path('en/logout/', views.en_logout_user, name="en_logout"),
    path('register/', views.es_register_user, name="es_register"),
    path('en/register/', views.en_register_user, name="en_register"),
    path('edit_profile/', views.es_edit_profile, name='es_edit_profile'),
    path('en/edit_profile/', views.en_edit_profile, name='en_edit_profile'),
    path('change_password', views.es_change_password, name='es_change_password'),
    path('en/change_password', views.en_change_password, name='en_change_password'),
]