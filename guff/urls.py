from django.urls import path
from django.contrib.auth import views as auth_views
from .import views 

urlpatterns = [ 
   path('',views.home,name= 'home'),
   
   path('register/',views.register, name='register'),
   path('login/',auth_views.LoginView.as_view(),name='login'),
   path('logout/',auth_views.LogoutView.as_view (),name='logout'),
   
   
path('post/create',views.post_create,name='post_create'),
path('post/<int:post_id>/edit/',views.post_edit, name='post_edit' ),
path('post/<int:post_id>/delete/',views.post_delete, name='post_delete'),

   
    
]