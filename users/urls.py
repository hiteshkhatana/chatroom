
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.login_view ),
    path('register/' , views.register_view ),
    path('logout/' , views.logout_view),
    path('detail/<int:pk>' , views.detail_view),
    path('home/', views.home_view),
    path('edit/', views.edit_view),
    path('getuserslist/', views.list_of_users),
    path('setprofile/' , views.setprofile)
]
