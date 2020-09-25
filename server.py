import socket

server = socket.socket(

    socket.AF_INET,
    socket.SOCK_STREAM,

)

server.bind(
    ('127.0.0.1', 9090)  # localhost
)

server.listen(1)
print('Server is listening')

while True:
    # ждем подключения
    user_socket, address = server.accept()
    print(f'User {address} connected')

    # отправляем данные
    user_socket.send('You are connected, bro'.encode('utf-8'))

    # принимаем данные
    data = user_socket.recv(2048)
    print(f'User {address}: ' + data.decode('utf-8'))



