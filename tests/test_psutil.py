import psutil
import socket

interfaces = psutil.net_if_addrs()

for interfaz, direcciones in interfaces.items():

    print(f"\nInterfaz: {interfaz}")

    for dato in direcciones:

        if dato.family == psutil.AF_LINK:
            print(f"MAC     : {dato.address}")

        if dato.family == socket.AF_INET:
            print(f"IPv4    : {dato.address}")
            print(f"Máscara : {dato.netmask}")