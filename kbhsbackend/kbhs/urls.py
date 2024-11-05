from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views
#change to specific location
from .views import redirect_to_nairobi

urlpatterns =[
    path('admissions/',views.create_admissions,name='create_admissions'),
    path('admissions/',views.list_admissions,name='list_admissions'),
    path('admissions/',views.update_admissions,name='update_admissions'),
    path('assignments/',views.list_assignment,name='list_assignment'),
    path('assignments/create/',views.create_assignment,name='create_assignment'),
    path('assignments/<int:id>/update/', views.update_assignment, name='update_assignment'),
    path('assignments/<int:id>/delete/', views.delete_assignment, name='delete_assignment'),
    path('redirect_to_nairobi/', redirect_to_nairobi, name='redirect_to_nairobi'),
    path('api-token-auth/',obtain_auth_token,name='api_token_auth'),
]    
   
