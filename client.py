import socket

client = socket.socket(

    socket.AF_INET,
    socket.SOCK_STREAM,

)

client.connect(
    ('10.8.67.204', 9090)
)

while True:
    # принимаем данные
    data = client.recv(2048)
    print(data.decode('utf-8'))

    # отпраляем данные
    while True:
            client.send(input("::: ").encode('utf-8'))
            data = client.recv(2048)
            print(data.decode('utf-8'))





