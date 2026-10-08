import random
so_bi_mat = random.randint(1, 100)

print("Máy tính đã chọn một số bí mật từ 1 đến 100. Hãy thử đoán")
while True:
        so_doan = int(input("Nhập số bạn đoán: "))
         if so_doan == so_bi_mat:
            print("Chúc mừng! Bạn đã đoán chính xác số bí mật.")
              break 
             elif so_doan < so_bi_mat:
              print(" Lớn hơn ")
             else:
               print(" Nhỏ hơn ")