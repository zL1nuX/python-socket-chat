import socket

client = socket.socket(

    socket.AF_INET,
    socket.SOCK_STREAM,

)

client.connect(
    ('127.0.0.1', 9090)
)

while True:
    # принимаем данные
    data = client.recv(2048)
    print(data.decode('utf-8'))

    # отпраляем данные
    client.send(input("::: ").encode('utf-8'))

