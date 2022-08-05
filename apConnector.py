import machine
import network

from establishConnection import establishConnection
from openSocket import openSocket
from serveData import serveData

def apConnector(data: object):
    try:
        ip = establishConnection()
        connection = openSocket(ip)
        serveData(connection, data)
    except KeyboardInterrupt:
        machine.reset()