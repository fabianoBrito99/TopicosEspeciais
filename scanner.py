import socket

def escanear_porta_tcp(ip, porta, tempo_espera=1):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soquete:
        soquete.settimeout(tempo_espera)
        resultado = soquete.connect_ex((ip, porta))
        if resultado == 0:
            return 'aberta'
        else:
            return 'fechada'

def escanear_porta_udp(ip, porta, tempo_espera=2):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as soquete:
        soquete.settimeout(tempo_espera)
        try:
            soquete.sendto(b'', (ip, porta))
            dados, _ = soquete.recvfrom(1024)
            return 'aberta'
        except socket.timeout:
            return 'filtrada'
        except Exception:
            return 'fechada'
