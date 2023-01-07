from django.urls import path
from .views import index, detail, create, newcreate, edit, delete, new_index

app_name = 'article'

urlpatterns = [
    path('', index, name='list'),
    path('article/detail/<slug:slug>/', detail, name='detail'),
    path('article/create/', create, name='create'),
    path('article/newcreate/', newcreate, name='newcreate'),
    path('article/edit/<slug:slug>/', edit, name='edit'),
    path('article/d/delete/<slug:slug>/', delete, name='delete'),
    path('new_edit/', new_index, name='new_index'),
]
