import socket


host = 'localhost'
port = 12345
bufsiz = 1024

if __name__=='__main__':
    client_socket = socket.socket(socket.AF_INET
            , socket.SOCK_STREAM)
    client_socket.connect((host,port))
    payload = 'GET TIME'

    while True:
        client_socket.send(payload.encode('utf-8'))
        data = client_socket.recv(bufsiz)
        print(data.decode('utf-8'))

        more_payload = input('enter END or payload: ')
        if more_payload == 'END':
            break
        else:
            client_socket.send(more_payload.encode('utf-8'))
    client_socket.close()
            
