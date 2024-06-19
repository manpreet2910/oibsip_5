import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 7777))

done = False
while not done:
    client.send(input("Message: ").encode('utf-8'))
    response = client.recv(1024).decode('utf-8')
    if response == 'exit':
        done = True
    else:
        print(response)

client.close()
