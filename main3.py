max = 0
min = 0
number = int(input("Nhập số lượng hóa đơn trong ca: "))
for i in range(1, number+1):
    input_day = int(input(f"Nhập giá trị hóa đơn ngày {i}: "))
    if i == 1 :
        min = input_day
    if input_day > max:
        max = input_day
    if input_day < min:
        min = input_day
print("-----KẾT QUẢ KIỂM TOÁN CA RIKKEI STORE----")
print("Hóa đơn có giá trị cao nhất: ", max)
print("Hóa đơn có giá trị nhỏ nhất: ", min)