from django.urls import path
from . import views


urlpatterns = [
	path ('', views.index, name="list"),
	# path ('/<str:pk>/', views.deleteTask, name="delete"),
	
	path('update_task/<str:pk>/', views.updateTask, name="update_task"),
	path('delete/<str:pk>/', views.deleteTask, name="delete"),
]

