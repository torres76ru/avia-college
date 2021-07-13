
from django.urls import path
from . import views

urlpatterns = [
	path('send_documents/', views.regform, name='regform'),
	path('reg/', views.reg, name='reg'),
	path('success/', views.success, name='success')
]
