from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader

import json

from .models import Message
# Create your views here.
def index(request):
    if 'msg' in request.GET:
        #print(request.GET['msg'])
        if len(request.GET['msg']) > 0:
            msg = Message()
            msg.text = request.GET['msg']
            msg.save()
        recent_msgs = Message.objects.order_by('-id')[:10]
        msg_list = []
        for m in recent_msgs:
            msg_list.append(m.text)
        #print({"msgs": msg_list})
        return JsonResponse({"msgs": msg_list})
    message_list = Message.objects.order_by('-id')[:10]
    template = loader.get_template('chat.html')
    context = {
        'message_list': message_list,
    }
    return HttpResponse(template.render(context, request))