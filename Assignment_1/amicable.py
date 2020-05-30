d = []
def sum_div(n) :
    sum = 1
    d.clear()
    for i in range(2, int(n**(0.5)) + 1):
        if n % i == 0:
            if n // i == i:
                d.append(i)
            else:
                d.append(i)
                d.append(n // i)
            i+=1
    for i in range(0, len(d)) :
        sum = sum + d[i]
    return sum

j = 1
h = 1
while j<=10 :
    s = sum_div(h)
    t = sum_div(s)
    if t==h and s>h:
         print(s, h)
         j +=1
    h+=1