#! /usr/bin/env python
# encoding:utf-8

import socket

socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_connection.connect(("192.168.1.106", 7171))

while True:
    message = socket_connection.recv(4096)
    decode_message = message.decode()
    print("Sunucu mesajı : " + decode_message)

    if decode_message == "0":
        print("Sunucu uygulamayı sonlandırdı.")
        break
        
    else:
        response = input("Cevabınızı yazın : ")
        encode_message = response.encode()
        socket_connection.send(encode_message)

socket_connection.close()