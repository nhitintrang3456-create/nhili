n = int(input())
so_uoc = 0 
for i in range (1,n+1) : 
    if n % i == 0 : 
        so_uoc += 1
    if so_uoc > 2 : 
        break 
if so_uoc == 2 : 
    print ("n la so nguyen to") 
else : 
    print ("n khong phai la so nguyen to ")