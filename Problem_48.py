# Power in Power

def last_10():
	result = 0
	for init in range(1, 1001):
		result += init**init

	return str(result)[-10::]

print(last_10())