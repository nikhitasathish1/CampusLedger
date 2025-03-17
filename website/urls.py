from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('record/<int:pk>/add_book/', views.add_book, name='add_book'),
    path('record/<int:pk>/delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('add_record/', views.add_record, name='add_record'),
]
