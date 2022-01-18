from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.index, name='index'),
    path('post_create/', views.post_create, name='post_create'),
    path('<int:post_id>/post_update', views.post_update, name='post_update'),
    path('<int:post_id>/post_delete', views.post_delete, name='post_delete'),
    path('<int:post_id>/comment_create', views.comment_create, name='comment_create'),
    path('<int:comment_id>/comment_delete', views.comment_delete, name='comment_delete'),
    path('<int:post_id>/post_image_like', views.post_image_like, name='post_image_like'),
    path('search/', views.search, name='search'),
    path('<int:user_id>/follow', views.follow, name='follow'),
    path('profile/', views.profile, name='profile'),
    path('<int:user_id>/profile/', views.other_profile, name='other_profile'),
    path('profile_update/', views.profile_update, name='profile_update'),
]
