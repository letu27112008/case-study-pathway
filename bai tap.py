# matkhau = input("nhap pass:")
# while matkhau == 'python':
#     print ('hello')
#     break
# else:
#     print ('nhap lai')

# n = int(input("nhap n :"))
# for i in range (2, n-1):
#     if n%i ==0:
#         print('ko la snt')
#         break
# else:
#         print('la snt')
# score = 0
# ans1 = input("Python duoc phat hanh vao nam nao A.1991, B.1989, C.2000, D.1995 ")
# if ans1 == 'A':
#         print('dung') 
#         score =score + 1
# ans2 = input("Ai la nguoi tao ra python A.Guido Van Rossum, B.Dennis Ritchie, C.James Gosling, D.Bjarne Stroustrup")
# if ans2 == 'A':
#         print('dung') 
#         score =score + 1
# ans3 = input("Cau len nao dung de hien thi du lieu ra man hinh trong python A.print(), B.cout<<, C.System, D.echo ")
# if ans3 == 'A':
#         print('dung') 
#         score =score + 1
# print (score)

print('chao mung ban den voi tro choi')
point = 0
ans1 = input("Con sông nào dài nhất bán đảo Đông Dương:\nA.Sông Hồng\nB.Sông Thầy\nC.Mê Kông\nD.Sông Ấn")
if ans1 == 'A':
    print("Dung")
    point = point + 1
    print("so diem hien tai cua ban la:",point)
else:
    print("Sai,cam on ban da den voii chuong trinh")
    quit()
    

ans2 = input("Tứ diện có bao nhiêu đường chéo:\nA.8\nB.4\nC.2\nD.Không có")
if ans2 == 'B':
    print("DUng")
    point = point +2
    print("so diem hien tai cua ban la:",point)
else:
    print("Sai") 
    point = point - point
    print("Sai,cam on ban da den voii chuong trinh")
    quit()
      
ans3 = input("Câu 3:Rắn có mấy lá phổi:\nA.2\nB.4\nC.1\nD.3") 
if ans3 == 'A':
    print("Dung")
    point =point +3
    print('so diem hien tai cua ban la:',point)
    q1 = input("ban co muon tiep tuc hay khong")
    if q1 =='Co':
        print("chung ta se den voi cau hoi thu 4")
    else:
        quit()
else:
    print("Sai")
    point = point - point

ans4 = input("Câu 4:Truyện Kiều có bao nhiêu câu thơ:\nA.3425\nB.3542\nC.3323\nD.3254")
if ans4 == 'A':
    print("Dung")
    point = point +4
    print("so diem cua ban la:",point)
else:
    print("Sai")
    point = point - point
    print("Sai,cam on ban da den voii chuong trinh")
    quit()
ans5 = input("cau 5:Hai điểm duy nhất của địa cầu không quay gọi là gì:\nA.Địa cực\nB.Trục\nC.Không có\nD.Chỉ có 1 điểm")
if ans5 == 'A':
    print("Dung")
    point = point +5
    q2 = input("ban co muon tiep tuc hay khong")
    print('so diem hien tai cua ban la:',point)
    if q2 =='Co':
        print("chung ta se den voi cau hoi thu 6")
    else:
        quit()
    
else:
    print("Sai")
ans6 = input("Cau 6:Loài trăn thường ngủ ở đâu\nA.Trên nệm\nB.Trên cây\nC.Trên đá\nD.Trong hang")
if ans6 == 'A':
    print("Dung")
    point = point +6

else:
    print("Sai")
    point = point - point
    print("Sai,cam on ban da den voii chuong trinh")
    quit()  

ans7 = input("cau 7:Nguyên nhân nào gây ra hiện tượng sóng thần ở biển:\nA.Gió lớn\nB.Bão\nC.Mưa\nD.Động đất")
if ans7 == 'A':
    print("Dung")
    point = point +7
    q3 = input("ban co muon tiep tuc hay khong")
    print('so diem hien tai cua ban la:',point)
    if q3 =='Co':
        print("chung ta se den voi cau hoi thu 8")
    else:
        quit()

else:
    print("Sai")
    point = point - point
    print("Sai,cam on ban da den voii chuong trinh")
    quit() 
ans8 = input("Cau8:Loài lưỡng cư nào thường xuất hiện và kêu to sau cơn mưa:\nA.Ếch\nB.Cóc\nC.Nhái\nD.Ễnh ương")
if ans8 == 'A':
    print("Dung")
    point = point +8

else:
    print("Sai")
    point = point - point
    print("Sai,cam on ban da den voii chuong trinh")
    quit()
ans9 = input("Cau 9:Châu lục nào có diện tích lớn nhất:\nA.Châu Á\nB.Châu Mỹ\nC.Châu Phi\nD.Châu Âu")
if ans9 == 'A':
    print("Dung")
    point = point +9
    q4 = input("ban co muon tiep tuc hay khong")
    print('so diem hien tai cua ban la:',point)
    if q4 =='Co':
        print("chung ta se den voi cau hoi thu 10")
    else:
        quit()
else:
    print("Sai")
    point = point - point
    print("Sai,cam on ban da den voii chuong trinh")
    quit()
    
ans10 = input("Cau 10:Công thức tính diện tích hình chữ nhật:\nA.a+b\nB.(a+b)x2\nC.a x b\nD.a-b")
if ans10 == 'A':
    print("Dung")
    point = point +10
    print("chuc mung ban da chien thang tro choi!,so diem cua ban la:",point)
else:
    print("Sai")
    point = point - point
    print("Sai,cam on ban da den voii chuong trinh")
    quit()
    

























# thislist = ["Con sông nào dài nhất bán đảo Đông Dương:A.Sông Hồng\nB.Sông Thầy\nC.Mê Kông\nD.Sông Ấn"]
# print(thislist)
 
