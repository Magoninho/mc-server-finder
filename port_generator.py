# This generates a list of ports to be used later on main.py

counter = 10968

with open("ports.txt", 'w') as f:
	for _ in range(9999 - 968):
		counter += 1
		f.write(str(counter) + "\n")