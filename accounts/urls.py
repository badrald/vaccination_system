from django.urls import path
from . import views


urlpatterns = [
    path('login',views.login_view,name='login_view'),
    path('',views.logout_view,name='logout'),
    path("profile/",views.profile_view,name='profile'),
    path('edit_profile/<int:id>',views.profile_edit,name="profile_edit"),
    path('profiles/',views.profiles_view,name="profiles"),
    path("delete_user/<int:id>",views.delete_user,name='delete_user'),
    path("password/<int:id>",views.change_password,name="change_password")
    
]
