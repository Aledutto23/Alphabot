import socket as sck

s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
s.connect(('192.168.0.126', 24000))
while True:
    istruzione = input("inserire un comando: ") #w, a, s, d, zig
    s.sendall(istruzione.encode())
s.close()