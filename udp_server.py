import socket

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")

# Bu bir veritabanı gibi çalışıyorca
di = {
    '17BIT0382': 'vivek',
    '17BEC0647': 'shikhar',
    '17BEC0150': 'tanveer',
    '17BCE2119': 'sahil',
    '17BIT0123': 'sidhant'
}

while True:
    # client'tan kullanıcı adını al
    name, addr1 = UDPServerSocket.recvfrom(bufferSize)

    # client'tan şifreyi al
    pwd, _ = UDPServerSocket.recvfrom(bufferSize)

    name = name.decode()
    pwd = pwd.decode()

    msg = ''
    flag = -1  # kontrol değişkeni

    if name not in di:
        msg = 'name does not exist'
        flag = 0
    else:
        for i in di:
            if i == name:
                if di[i] == pwd:
                    msg = "pwd match"
                    flag = 1
                else:
                    msg = "pwd wrong"
                break  # doğru kullanıcı bulunduğunda döngüyü durdur

    bytesToSend = str.encode(msg)
    UDPServerSocket.sendto(bytesToSend, addr1)
