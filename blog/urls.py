from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('category/<slug:category_slug>/', views.post_list, name='post_list_by_category'),
    path('tag/<str:tag>/', views.post_list_by_tag, name='post_list_by_tag'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/comment/', views.add_comment, name='add_comment'),
]