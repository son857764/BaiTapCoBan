#Viết chương trình chấp nhận một chuỗi số, phân tách bằng 
# dấu phẩy từ giao diện điều khiển, tạo ra một danh sách
#  và một tuple chứa mọi số.

value = input("Nhập vào các chuỗi số: ")
list = value.split(",")
tuple = tuple(value.split(","))
print(list)
print(tuple)