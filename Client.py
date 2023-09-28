import socket
import time

server_ip_address = "192.168.56.1"
port_number = 2022
message_size = 100000
message_format = 'utf-8'
client = socket.socket()
client.connect((server_ip_address, port_number))


def send(msg):
    message = msg.encode(message_format)
    client.send(message)


print("--Connected to server--")
print("To sending information to server, insert number of students and then,"
      "\ninsert every student information separated by space and press 'Enter'\n")

student_count = int(input("insert number of students: "))
for i in range(0, student_count):
    data = input("Student-" + str(i+1) + "  ")
    send(data)

print("\n--Information sent to server successfully--")
print("Chose on of 'Average', 'Max', 'Min', 'Sort' and type it to see the result,"
      "\ntype 'Exit' to disconnect from server and close the program")

while True:
    data = input("\nChoose the operation: ")
    if data == "Average":
        send(data)
        for i in range(0, student_count):
            print(client.recv(message_size).decode(message_format))
            send("received")
    elif data == "Max":
        send(data)
        print(client.recv(message_size).decode(message_format))
    elif data == "Min":
        send(data)
        print(client.recv(message_size).decode(message_format))
    elif data == "Sort":
        send(data)
        for i in range(0, student_count):
            print(client.recv(message_size).decode(message_format))
            send("received")
    elif data == "Exit":
        send(data)
        print("\n\ndisconnecting from server...")
        time.sleep(4)
        break
    else:
        print("Operation is not valid")

