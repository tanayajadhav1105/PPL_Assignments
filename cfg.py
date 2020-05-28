r = ["tiger", "grass", "goat"]
l = []

def game(a):
    x = 1
    if len(a) == 2:
        if "grass" in a and "goat" in a:
            x = 0
        elif "tiger" in a and "goat" in a:
            x = 0
    else:
        x = 1
    return x

while r!=[]:
    for i in range(0,len(r)):
        if i >= len(r):
            break
        p = r[i]
        q = i
        r.remove(p)
        if game(r) == 0:
            r.insert(q,p)
            continue
        l.append(p)
        print("Take " + p + " from right to left")
        if game(l) == 0:
            s = l[0]
            l.remove(s)
            r.append(s)
            print("Take " + s + " from left to right")
            break

