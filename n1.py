MOD = 10**9+7
T = int(input())
for _ in range (T) : 
    N,K = map (int,input().split())
    ket_qua = pow(N,K,MOD)
    print (ket_qua)
