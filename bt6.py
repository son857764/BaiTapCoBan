import re
########### in kết quả ra 1 chuỗi:Hàm số re.sub() ,re.search()
s1 = '1ab23cdef456'
m1 = re.sub(r'\D','', s1)
print(m1)
#>> 123456

s2 = 'Thứ 6 ngày 25 tháng 6 năm 2021, 21:30'
m2 = re.sub(r'\D','', s2)  
print(m2)
#>> 625620212130

s1 = '1ab23cdef456'
m1 = re.search(r'\d', s1)
print(m1)
#>> <re.Match object; span=(0, 1), match='1'>

print(m1.group())
#>> 1

s2 = 'Thứ 6 ngày 25 tháng 6 năm 2021, 21:30'
m2 = re.search(r'\d', s2)  
print(m2.group())
#>> 6

s = 'Năm 2021, thứ 6 ngày 13 21:30'
m = re.search(r'\d+', s)  
print(m)
#>> <re.Match object; span=(4, 8), match='2021'>

print(m.group())
#>> 2021

#Lấy vị trí xuất hiện của dãy số
print(m.start())
#>> 4

#Lấy vị trí kết thúc của dãy số
print(m.end())
#>> 8







########## in kết quả ra 1 list:re.findall()
s1 = '1ab23cdef456'
m1 = re.findall(r'\d', s1)  
print(m1)
#>> ['1', '2', '3', '4', '5', '6']

s2 = 'Thứ 6 ngày 25 tháng 6 năm 2021, 21:30'
m2 = re.findall(r'\d', s2)                  #tách riêng
print(m2)
#>> ['6', '2', '5', '6', '2', '0', '2', '1', '2', '1', '3', '0']

s = 'Thứ 6 ngày 25 tháng 6 năm 2021, 21:30'
m = re.findall(r'\d+', s)                   #số liền nhau
print(m)
#>> ['6', '25', '6', '2021', '21', '30']
