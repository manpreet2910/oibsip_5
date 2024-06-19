import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("localhost", 7777))
server.listen()
print("Manpreet's Server listening on port 7777")

client, addr = server.accept()
print(f"Connection established with {addr}")

done = False
while not done:
    txt = client.recv(1024).decode('utf-8')
    if txt == 'exit':
        done = True
    else:
        print(txt)
    client.send(input("Message: ").encode('utf-8'))

client.close()
server.close()
