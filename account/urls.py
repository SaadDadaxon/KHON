from django.urls import path
from .views import login_views, logout_views, register_views


app_name = 'account'


urlpatterns = [
    path('login/', login_views, name='login'),
    path('logout/', logout_views, name='logout'),
    path('register/', register_views, name='register'),
]
