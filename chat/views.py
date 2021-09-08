from django.shortcuts import redirect, render
from .models import ChatRoom
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/')
def join_view(request):

    if request.method=="POST":
        room_name = request.POST['room']

        return redirect(f'/chat/{room_name}/')

    return render(request,'chat/joinroom.html')

@login_required(login_url='/')
def create_view(request):
    
    if request.method=="POST":
        room_name = request.POST['room']

        return redirect(f'/chat/{room_name}/')

    return render(request,'chat/createroom.html')

@login_required(login_url='/')
def chatroom_view(request , room_name):
    objs = ChatRoom.objects.filter(room = room_name)

    if objs is None:
        ChatRoom.objects.create(username = request.user, message = "created this chatroom" , room = room_name)
        objs = ChatRoom.objects.filter(room = room_name)
    

    context = {
        'room' : room_name,
        'chats' : objs
    }


    return render(request, 'chat/chatroom.html' , context)