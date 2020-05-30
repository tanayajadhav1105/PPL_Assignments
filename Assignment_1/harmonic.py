d = []
j = 1
def harm_mean(n) :
	d.clear()
	for i in range(1, int(n**(0.5)) + 1):
		if n % i == 0:
			if n // i == i:
				d.append(i)
			else:
				d.append(i)
				d.append(n // i)
	sum = 0
	l = len(d)
	for i in range(0, l) :
		sum = sum + (n/d[i])
	m = l/sum
	m *= n
	return m
h = 1

while j<=10 :
	mean = harm_mean(h)
	if mean.is_integer() == True :
		print(h)
		j+=1
	h+=1