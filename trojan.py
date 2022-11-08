#! /usr/bin/env python
# encoding:utf-8
import socket

socket_connection=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_connection.connect(("192.168.1.106", 7171))

socket_connection.close()