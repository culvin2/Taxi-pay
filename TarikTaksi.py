a = int(input())
for i in range(a):
    A,B,C = (map(int,input().split()))
    if C >2000:
        b = C - 2000
        c = B*b/100
        t = A + c
        print(int(t))
    else:
        print(A)



