from django.urls import path
from . import views


urlpatterns =[
    path('assignments/',views.list_assignment,name='list_assignment'),
    path('assignments/create/',views.create_assignment,name='create_assignment'),
    path('assignments/<int:id>/update/', views.update_assignment, name='update_assignment'),
    path('assignments/<int:id>/delete/', views.delete_assignment, name='delete_assignment'),
]    
   
