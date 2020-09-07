from collections import defaultdict

def apache_log_reader(log_file="access.log"):
	ips = defaultdict(int)
	with open(log_file) as f:
		lines = f.readlines()

	for line in lines:
		ips[line.split()[0]] += 1

	return ips



print(apache_log_reader())