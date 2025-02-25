from django.urls import path
from . import views


urlpatterns = [
    path('user/', views.create_user, name='create-user'),
    path('logout/', views.logout_user_manager, name='logout'),
    path('update/', views.update, name="update"),
    path('update_user/<int:pk>/', views.update_user, name='update_user'),
]
