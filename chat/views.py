from django.shortcuts import redirect, render
from .models import ChatRoom , Privatenotifications
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format

from django.contrib import messages
from django.db.models import Q
import json


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
        'chats' : objs[1:]
    }

    return render(request, 'chat/chatroom.html' , context)

@login_required(login_url='/')
def privateroom_view(request , currentuser , targeted):
        

    if request.user.username == currentuser or request.user.username == targeted:

        room_name = f"{currentuser}-{targeted}"
        reverse_name = f"{targeted}-{currentuser}"

        
        objs = ChatRoom.objects.filter(Q(room = room_name) | Q(room = reverse_name))

        if not objs:
            ChatRoom.objects.create(username = request.user, message = "created this chatroom" , room = room_name)
            objs = ChatRoom.objects.filter(room = room_name)

        pnotifications = Privatenotifications.objects.filter(sender = currentuser , receiver = targeted , seen = False)

        if not pnotifications:
            Privatenotifications.objects.create(sender = currentuser , receiver = targeted)


        
        context = {
            'currentuser' : currentuser,
            'targeted' : targeted,
            'room' : objs.values()[0]['room'],
            'chats' : objs[1:]
        }

        return render(request, 'chat/privateroom.html' , context)

    else:
        messages.info(request , "You cannot access this chatroom!!")
        return redirect('/')

def allnotifications(request):

    objs = Privatenotifications.objects.filter(receiver = request.user , seen = False)
    
    return JsonResponse(list(objs.values()) , safe = False)


def seenstatus(request):
    
    sender = request.POST['sender']
    receiver = request.POST['receiver']
    
    obj = Privatenotifications.objects.get(sender = sender , receiver = receiver , seen = False)

    obj.seen = True
    obj.save()

    return JsonResponse("success" , safe = False)

def deletemessage(request):

    username = request.POST['username']
    message = request.POST['message']

    obj = ChatRoom.objects.get(username = username, message = message)
    obj.delete()

    return JsonResponse("success" , safe = False)


def uploadimages(request):
    
    img = request.FILES['file']
    username = request.POST['username']
    room = request.POST['room']

    obj = ChatRoom.objects.create(room = room , username = username , img = img)
    obj.save()

    date = DateFormat(obj.date)
    date = date.format(get_format('DATETIME_FORMAT')) 
   
   

    
    return JsonResponse( {'username' : obj.username , 'img' : obj.img.url , 'date' : date } , safe=False)


