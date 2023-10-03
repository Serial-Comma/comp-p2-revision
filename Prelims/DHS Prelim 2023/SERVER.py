import socket
import csv
import datetime

server = "127.0.0.1"
port = 9999
ADDR  = (server,port)

def decrypt(ciphertext):
    ciphertext = list(ciphertext)
    # print(ciphertext)
    length = len(ciphertext)
    output = ''
    for i in range(len(ciphertext)):
        x = ciphertext[i]
        # print(x,ord(x),)
        x = ord(x)

        if x-length < 32:
            x = (x-length) + 126 -31
        else:
            x = (x-length)
        # print(x,chr(x),"\n")
        length -=1
        output+= chr(x)
    return output

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


connected = True
print('''-------------------
SERVER OPEN
-------------------
''')

while connected == True:
    server.listen()
    conn,addr = server.accept()

    print('''
Waiting For message
------------------- 
          ''')
    x = conn.recv(2048).decode()
    conn.close() 
    if x:
        x = x.strip('\n')
        decrypted = decrypt(x)
        print(f"Encrypted message: {x}")
        print(f"Decrypted message: {decrypted}")
        with open ("./LOG.csv",'a') as f:
            file = csv.writer(f)
            date = datetime.datetime.now()
            dates=(f"{date.day}-{date.month}-{date.year} {date.hour}:{date.minute}:{date.second}")
            file.writerow([date,addr[0],addr[1],x,decrypted])
        
        continues = input('''
    -------------------                       
    Do you want to continue listening? [Y/N]''')
        if continues.upper() == "Y":
            pass
        else:
            connected = False
               
print('''-------------------
SERVER CLOSED
-------------------
''')




    