# This script will find opened ports in a bunch of ngrok ip addresses
# and then write the found IPs to open_servers.txt

import socket, os

progress = 0

def is_open(port):

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	result = sock.connect_ex(('0.tcp.sa.ngrok.io', port))

	return True if result == 0 else False

with open('ports.txt', 'r') as f:
	ports = f.read().splitlines()
	
	with open('open_servers.txt', 'w') as b:
		for p in ports:
			current_port = int(p)
			if is_open(current_port):
				b.write(f"0.tcp.sa.ngrok.io:{current_port}\n")
				progress += 1
				os.system("clear")
				print(f"{progress} servers found...")
			else:
				continue
			


# 14457