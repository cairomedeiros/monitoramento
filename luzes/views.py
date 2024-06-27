from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Luz

def controlar_luz(request, luz_id, action):
    luz = get_object_or_404(Luz, id=luz_id)
    if action == 'on':
        luz.status = True
    elif action == 'off':
        luz.status = False
    luz.save()
    return JsonResponse({'status': luz.status})

def set_brilho(request, light_id, brilho):
    luz = get_object_or_404(Luz, id=light_id)
    luz.brilho = brilho
    luz.save()
    return JsonResponse({'brilho': luz.brilho})

