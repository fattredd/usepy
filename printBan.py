import sys, pickle

def pBan(data):
	data=data.replace('\r','')
	for line in data:
		for char, count in line:
			sys.stdout.write(char * count)
		sys.stdout.write("\n")

def pLoad(name):
	if not '.p' in name:
		name += '.p'
	f = open(name)
	out = pickle.loads(f.read())
	f.close()
	return out