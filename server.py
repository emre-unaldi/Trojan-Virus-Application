#! /usr/bin/env python
# encoding:utf-8
import socket

socket_connection=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

socket_connection.bind(("192.168.1.106", 7171))
socket_connection.listen(1)

print("Hedef sistemin bağlantı kurması bekleniyor...")
kurban, ip=socket_connection.accept()

print("Hedef sistem ile bağlantı sağlandı.")
print("Hedef sistem bilgileri : %s" % str(ip))

socket_connection.close()