# Với số nguyên n nhất định, hãy viết chương trình để 
# tạo ra một dictionary chứa (i, i*i) như là số nguyên 
# từ 1 đến n (bao gồm cả 1 và n) sau đó in ra dictionary
#  này. Ví dụ: Giả sử số n là 8 thì đầu ra sẽ là:
#  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}.

dict = dict() # Khai báo thư viện rỗng, chưa chứa phần tử nào

n = int(input("Số nguyên n = ")) # nhập vào số nguyên n
for i in range(1,n+1):
    dict[i] = i**2
    # vòng lặp thêm phần tử thứ i vào dictionary
print(dict) #in ra dictionary