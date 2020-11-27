import socket

 

localIP     = "127.0.0.1"

localPort   = 20001

bufferSize  = 1024

 

msgFromServer       = "Hello UDP Client"

bytesToSend         = str.encode(msgFromServer)

 

# Crea un socket de datagrama

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Enlaza la dirección y la IP

UDPServerSocket.bind((localIP, localPort))

 

print("UDP server up and listening")

 

# Escucha los datagramas entrantes del cliente

while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)

   

    # Envía una respuesta al cliente

    UDPServerSocket.sendto(bytesToSend, address)
