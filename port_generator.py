# This generates a list of ports to be used later on main.py

counter = 10000

with open("ports.txt", 'w') as f:
	for _ in range(20000 - counter):
		counter += 1
		f.write(str(counter) + "\n")
