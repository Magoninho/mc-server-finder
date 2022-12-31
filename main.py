# This script will find opened ports in a bunch of ngrok ip addresses
# and then write the found IPs to open_servers.txt

import os
from mcstatus import JavaServer

# server = JavaServer.lookup("mc.hypixel.nett")


# try:
# 	status = server.status()
# 	print("deu certo")
# except:
# 	print("fudeu")

number = input("server number: ")
region = input("server region [sa, eu, ap, au]: ")


progress = 0


def is_open(server_ip):
    server = JavaServer.lookup(server_ip)

    try:
        server.status()  # check if the server is on minecraft
        return True
    except:
        # if it gives an error, the server does not exist
        return False


with open("ports.txt", "r") as f:
    ports = f.read().splitlines()

    with open("open_servers.txt", "w") as b:
        for p in ports:
            # for number in [0, 2, 6, 7, 8]:
            current_port = int(p)
            server_ip = f"{number}.tcp.{region}.ngrok.io:{current_port}"
            if is_open(server_ip):
                b.write(f"{server_ip}\n")
                progress += 1
                # os.system("clear")
                print(f"{progress} servers found... [{server_ip}]")
            else:
                continue
