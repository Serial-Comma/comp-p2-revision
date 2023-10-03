def encrypt(plaintext):
    plaintext = list(plaintext)
    length = len(plaintext)
    output = ''
    for i in range(len(plaintext)):
        x = plaintext[i]
        # print((x,ord(x),length))
        x = ord(x)
        if x+length > 126:
            x = (x+length) % 126 +31
        else:
            x = (x+length)
        length -=1
        output+= chr(x)
    return output

#main program
import socket

print("-------------------")
print("CLIENT OPEN")
print("-------------------")
print()

my_socket = socket.socket()
my_socket.connect(('127.0.0.1', 9999))

message = input("Enter message: ")
encrypted_message = encrypt(message)
# print(encrypted_message)

data = encrypted_message.encode()
my_socket.sendall(data + b'\n')
print("message sent")
my_socket.close()

print("-------------------")
print("CLIENT CLOSED")
print("-------------------")
