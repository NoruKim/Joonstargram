from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("users/", views.CurrentUserAPIView.as_view(), name="current-user"),
    # path('', views.main, name='main'),
    path('signup/', views.signup, name='signup'),
    path('logout/' , views.logout, name='logout'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name="activate"),
]
