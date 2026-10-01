T = int(input())
for _ in range (T) :
    n,X = map(int,input().split())
    A = list (map(int,input().split()))
    if X in A : 
        print (1)
    else : 
        print (-1)

