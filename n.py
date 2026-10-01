# số lần đếm 
T = int(input())
for _ in range (T) : 
    N,X = map(int,input().split ())
    A = list(map(int,input().split()))
    count = A.count(X)
    if count > 0 : 
        print(count)
    else :
        print(-1)

