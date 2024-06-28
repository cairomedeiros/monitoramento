from phue import Bridge
import os

BRIDGE_IP = os.getenv("BRIDGE_IP")
bridge = Bridge(BRIDGE_IP)

# Se for a primeira vez, você precisa pressionar o botão no hub e rodar o seguinte:
# bridge.connect()