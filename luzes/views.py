from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import render

from phue import Bridge
import firebase_admin
from firebase_admin import credentials, firestore
import os

# Configuração do Firebase
BASE_DIR = os.environ.get(r"BASE_DIR")
FIREBASE_CREDENTIALS = os.path.join(BASE_DIR, os.environ.get("FIREBASE_CREDENTIALS"))
cred = credentials.Certificate(FIREBASE_CREDENTIALS)
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

# Cliente do Firestore
db = firestore.client()

# Configuração do Philips Hue
BRIDGE_IP = os.environ.get("IP_HUB") # Substitua pelo IP do seu hub
bridge = Bridge(BRIDGE_IP)

def controlar_luz(request, luz_id, action):
    luz_ref = db.collection('luzes').document(str(luz_id))
    if action == 'on':
        luz_ref.set({'status': True}, merge=True)
        bridge.set_light(luz_id, 'on', True)
    elif action == 'off':
        luz_ref.set({'status': False}, merge=True)
        bridge.set_light(luz_id, 'on', False)
    luz = luz_ref.get().to_dict()
    return JsonResponse({'status': luz['status']})

def set_brilho(request, luz_id, brilho):
    luz_ref = db.collection('luzes').document(str(luz_id))
    luz_ref.set({'brilho': brilho}, merge=True)
    bridge.set_light(luz_id, 'bri', int(brilho * 2.54))
    luz = luz_ref.get().to_dict()
    return JsonResponse({'brilho': luz['brilho']})

def listar_luzes(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        luzes_ref = db.collection('luzes')
        luzes = [luz.to_dict() for luz in luzes_ref.stream()]
        return JsonResponse(luzes, safe=False)
    else:
        return render(request, 'luzes/index.html')

