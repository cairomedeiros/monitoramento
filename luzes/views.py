from django.http import JsonResponse
from django.conf import settings

import firebase_admin
from firebase_admin import credentials, firestore
import os

# Configuração do Firebase
BASE_DIR = r'C:\\Users\\cairo\\Downloads'
FIREBASE_CREDENTIALS = os.path.join(BASE_DIR, 'monitoramento-d65a9-firebase-adminsdk-nkhs7-e864dfbe22.json')
cred = credentials.Certificate(FIREBASE_CREDENTIALS)
firebase_admin.initialize_app(cred)

# Cliente do Firestore
db = firestore.client()

def controlar_luz(request, luz_id, action):
    luz_ref = db.collection('luzes').document(str(luz_id))
    if action == 'on':
        luz_ref.set({'status': True}, merge=True)
    elif action == 'off':
        luz_ref.set({'status': False}, merge=True)
    luz = luz_ref.get().to_dict()
    return JsonResponse({'status': luz['status']})

def set_brilho(request, luz_id, brilho):
    luz_ref = db.collection('luzes').document(str(luz_id))
    luz_ref.set({'brilho': brilho}, merge=True)
    luz = luz_ref.get().to_dict()
    return JsonResponse({'brilho': luz['brilho']})

def listar_luzes(request):
    luzes_ref = db.collection('luzes')
    luzes = [luz.to_dict() for luz in luzes_ref.stream()]
    return JsonResponse(luzes, safe=False)

