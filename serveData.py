from createResponse import createResponse

def serveData(connection: object, data: object):
    responseTemplate = createResponse(data)
    headers = {"Content-Type": "application/json; charset=utf-8"}
    
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        
        client.send('HTTP/1.0 200 OK\r\nContent-type: application/json\r\n\r\n')
        client.send(str(responseTemplate))                
        client.close()
