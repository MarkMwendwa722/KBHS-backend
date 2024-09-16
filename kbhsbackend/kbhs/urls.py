from django.urls import path
from . import views


urlspatterns = [
path('', views.Home)
# path('', views.Home, name='home')
# path('contactus/', views.ContactUs)
]
