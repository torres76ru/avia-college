from django.urls import path
from . import views

urlpatterns = [
	path('send/', views.send, name='send'),
	path('cancel/', views.cancel, name='cancel'),
]