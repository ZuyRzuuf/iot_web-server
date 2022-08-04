import network

try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

def estabilishConnection():
    wlan = network.WLAN(network.STA_IF)

    if not wlan.isconnected():
        print('connecting to network...')
        wlan.active(True)
        wlan.connect(secrets["ssid"], secrets["password"])

        while not wlan.isconnected():
            pass
        
        print('network config:', wlan.ifconfig())
