import json
import machine
import network
import socket
from response import response

try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

def establishConnection() -> str:
    wlan = network.WLAN(network.STA_IF)

    if not wlan.isconnected():
        print('connecting to network...')
        wlan.active(True)
        wlan.connect(secrets["ssid"], secrets["password"])

        while not wlan.isconnected():
            pass
        
    ip = wlan.ifconfig()[0]
    print('ip: ', ip)
        
    return ip

def openSocket(ip: str) -> object:
    address = (ip, 80)
    connection = socket.socket()
    
    connection.bind(address)
    connection.listen(1)
    
    print('listening on', address)
    
    return connection

def createResponse() -> str:
    return str(response)

def serveData(connection: object):
    dataMock = {
        "temperature": 34,
        "humidity": "55%"
    }
    
    responseTemplate = createResponse(dataMock)
    headers = {"Content-Type": "application/json; charset=utf-8"}
    
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        
        client.send('HTTP/1.0 200 OK\r\nContent-type: application/json\r\n\r\n')
        client.send(str(responseTemplate))                
        client.close()

def createResponse(dataMock: dict) -> dict:
    try:
        templateFile = open("response.json", "r")
    except:
        print("Response template is kept in response.json file, please add them there!")
        raise
        
    responseTemplate = json.load(templateFile)
    templateFile.close()
    
    for k, v in responseTemplate.items():
        if k in dataMock:
            responseTemplate.update({k:dataMock[k]})
    
    return responseTemplate

try:
    ip = establishConnection()
    connection = openSocket(ip)
    serveData(connection)
except KeyboardInterrupt:
    machine.reset()