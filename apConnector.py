import machine
import network

from establishConnection import establishConnection
from openSocket import openSocket
from serveData import serveData

data = {
    "temperature": 38,
    "humidity": "45%"
}
    
try:
    ip = establishConnection()
    connection = openSocket(ip)
    serveData(connection, data)
except KeyboardInterrupt:
    machine.reset()