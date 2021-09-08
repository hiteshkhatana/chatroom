from django.urls import path
from . import views

urlpatterns = [
    path('join/' , views.join_view ),
    path('create/' , views.create_view ),
    path('<room_name>/', views.chatroom_view),
    
]
