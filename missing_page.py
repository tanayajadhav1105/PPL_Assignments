l = []
missl = []
print("Enter List of pages of book. Press 0 to end list\n")
while 1 :
	x = input()
	if x == '0' :
		break

	if '-' in x :
		y = x.split('-')
		z = int(y[0])
		while z <= int(y[1]) :
			l.append(z)
			z+=1
	else :
		l.append(int(x))
l.sort
for x in range(1, l[-1]+1) :
	if x not in l :
		missl.append(x)
i = l[-1]+1
while i<=25 :
	missl.append(i)
	i+=1
print("The list of missing pages is : \n")
print(missl)