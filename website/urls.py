
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home,name = 'home'),
    path('logout/',views.logout_user,name = 'logout'),
    path('register/',views.register_user,name = 'register'),
    path('records/',views.Records_view, name="records"),
    path('manage_records/',views.manage_Records, name="manage_records"),
    path('view_person/<int:pk>/',views.view_person, name="view_person"),
    path('add_records/',views.add_records, name="add_records"),

    
]