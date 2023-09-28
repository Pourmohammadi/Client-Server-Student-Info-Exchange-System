import socket
import threading
import os

port_number = 2022
server_ip_address = socket.gethostbyname(socket.gethostname())
server_socket = socket.socket()
server_socket.bind((server_ip_address, port_number))
message_size = 100000
message_format = 'utf-8'
data_base = {}


def connection_controller(connection, address):
    data_base[address] = []
    while True:
        message = connection.recv(message_size).decode(message_format)
        if message and (message != "Max" and message != "Min" and
                        message != "Sort" and message != "Exit" and message != "Average"):
            data_base[address].append(message.split())
        else:
            for i in data_base[address]:
                grades_average = (float(i[4]) + float(i[5]) + float(i[6]) + float(i[7]) + float(i[8]))/5
                i.append(grades_average)
            data_base[address].sort(key=lambda row: (row[9]), reverse=False)
            if message == "Max":
                result = str(data_base[address][-1][0]) + " " + str(data_base[address][-1][1]) +\
                         " " + str(data_base[address][-1][9])
                connection.send(result.encode(message_format))
            elif message == "Min":
                result = str(data_base[address][0][0]) + " " + str(data_base[address][0][1]) +\
                         " " + str(data_base[address][0][9])
                connection.send(result.encode(message_format))
            elif message == "Average":
                for i in data_base[address]:
                    result = str(i[2]) + " " + str(i[9])
                    connection.send(result.encode(message_format))
                    connection.recv(message_size)
            elif message == "Sort":
                for i in data_base[address]:
                    result = str(i[3]) + " " + str(i[9])
                    connection.send(result.encode(message_format))
                    connection.recv(message_size)
            elif message == "Exit":
                break

    connection.close()


def make_connection():
    server_socket.listen()
    department_number = int(input("Enter number of departments: "))
    for i in range(0, department_number):
        os.system("start /B start cmd.exe @cmd /c python Client.py")
        connection, address = server_socket.accept()
        thread = threading.Thread(target=connection_controller, args=(connection, address))
        thread.start()


make_connection()
