import socket

def openSocket(ip: str) -> object:
    address = (ip, 80)
    connection = socket.socket()
    
    connection.bind(address)
    connection.listen(1)
    
    print('listening on', address)
    
    return connection
