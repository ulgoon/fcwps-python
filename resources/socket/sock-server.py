import socket
from time import ctime


host = 'localhost'
port = 12345
bufsiz = 1024
addr = (host, port)

if __name__=='__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(addr)
    server_socket.listen(5)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    while True:
        print("Server is now listening..")
        client_sock, sock_addr = server_socket.accept()
        print("Client is now connected!!")
        while True:
            data = client_sock.recv(bufsiz)
            print(data)
            if not data or data=='END':
                break
            elif data.decode('utf-8') == 'GET TIME':
                print('received: {}'.format(data.decode('utf-8')))
                to_send = ctime()
                try:
                    client_sock.send(to_send.encode('utf-8'))
                except:
                    print('send failed')

        client_sock.close()
    server_socket.close()





