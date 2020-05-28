def luDecomposition(m, n):
    l = [[0 for x in range(n)] for y in range(n)]
    u = [[0 for x in range(n)] for y in range(n)]
    for i in range(n) :
        for k in range(i, n):
            sum = 0
            for j in range(i):
                sum += (l[i][j] * u[j][k])
            u[i][k] = m[i][k] - sum
        for k in range(i, n):
            if (i == k):
                l[i][i] = 1
            else:
                sum = 0
                for j in range(i):
                    sum += (l[k][j] * u[j][i])
                l[k][i] = int((m[k][i] - sum) // u[i][i])
    print("Lower Triangular\tUpper Triangular")
    for i in range(n):
        for j in range(n):
            print(l[i][j], end = " ")
        print("\t\t", end = "\t")
        for j in range(n):
            print(u[i][j], end = " ")
        print("")

n = int(input("Enter order of matrix : "))
ma = [[0 for x in range(n)] for y in range(n)]
for i in range(0, n):
    for j in range(0, n):
        ma[i][j] = int(input())
luDecomposition(ma, n);