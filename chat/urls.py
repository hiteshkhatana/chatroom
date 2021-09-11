from django.urls import path
from . import views

urlpatterns = [
    path('join/' , views.join_view ),
    path('create/' , views.create_view ),
    path('<room_name>/', views.chatroom_view),
    path('private/<currentuser>-<targeted>/' , views.privateroom_view),
    path('get/notifications/', views.allnotifications),
    path('get/seenstatus/', views.seenstatus),
    path('get/delete/' , views.deletemessage),
    path('upload/images/' , views.uploadimages)
    
]
