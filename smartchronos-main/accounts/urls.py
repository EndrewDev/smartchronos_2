from django.urls import path
from . import views


urlpatterns = [
    path('user/', views.create_user, name='create-user'),
    path('logout/', views.logout_user_manager, name='logout'),
    path('update-user/<int:user_id>/', views.update_user, name="update"),
]
