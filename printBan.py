import sys

def pBan(data):
	for line in data:
		for char, count in line:
			sys.stdout.write(char * count)
		sys.stdout.write("\n")