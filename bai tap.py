import random
print('chao mung ban den voi tro choi')
point = 0
while True:
    question1="Con sông nào dài nhất bán đảo Đông Dương:\nA.Sông Hồng\nB.Sông Thầy\nC.Mê Kông\nD.Sông Ấn"
    print(question1)
    ans1 = input('nhap A,B,C,D: ')
    if ans1.upper() == 'A':
        sure=input('ban co chot dap an nay hay khong (Co/khong) ? ')
        if sure== 'Co':
            print("Dung")
            point = point + 1
            print("so diem hien tai cua ban la:",point)
            break
    elif ans1 =='B' or ans1=='C' or ans1 =='D':
             sure=input('ban co chot dap an nay hay khong (Co/khong) ? ')
             if sure== 'Co':
                print("Sai,cam on ban da den voii chuong trinh")
                quit()

    


        
        

ans2 = input("Tứ diện có bao nhiêu đường chéo?\nA.8\nB.4\nC.2\nD.Không có")
if ans2.upper() == 'A':
    print("Dung")
    point = point +2
    print("so diem hien tai cua ban la:",point)
else:
    print("Sai") 
    point = point - point
    print("Sai,cam on ban da den voii chuong trinh")
    quit()
      
ans3 = input("Câu 3:Rắn có mấy lá phổi?\nA.2\nB.4\nC.1\nD.3") 
if ans3.upper() == 'A':
    print("Dung")
    point =point +3
    print('so diem hien tai cua ban la:',point)
    q1 = input("ban co muon tiep tuc hay khong ")
    if q1 =='Co':
        print("chung ta se den voi cau hoi thu 4")
    else:
        quit()
else:
    print("Sai")
    point = point - point

ans4 = input("Câu 4:Truyện Kiều có bao nhiêu câu thơ?\nA.3425\nB.3542\nC.3323\nD.3254")
if ans4.upper() == 'A':
    print("Dung")
    point = point +4
    print("so diem cua ban la:",point)
else:
    print("Sai")
    point = point - point
    print("Sai,cam on ban da den voii chuong trinh")
    quit()
ans5 = input("cau 5:Hai điểm duy nhất của địa cầu không quay gọi là gì?\nA.Địa cực\nB.Trục\nC.Không có\nD.Chỉ có 1 điểm")
if ans5.upper() == 'A':
    print("Dung")
    point = point +5
    q2 = input("ban co muon tiep tuc hay khong ")
    print('so diem hien tai cua ban la:',point)
    if q2.upper() =='Co':
        print("chung ta se den voi cau hoi thu 6")
    else:
        quit()
    
else:
    print("Sai")
ans6 = input("Cau 6:Loài trăn thường ngủ ở đâu?\nA.Trên nệm\nB.Trên cây\nC.Trên đá\nD.Trong hang")
if ans6.upper() == 'A':
    print("Dung")
    point = point +6

else:
    print("Sai")
    point = point - point
    print("Sai,cam on ban da den voii chuong trinh")
    quit()  

ans7 = input("cau 7:Nguyên nhân nào gây ra hiện tượng sóng thần ở biển?\nA.Gió lớn\nB.Bão\nC.Mưa\nD.Động đất")
if ans7.upper() == 'A':
    print("Dung")
    point = point +7
    q3 = input("ban co muon tiep tuc hay khong ")
    print('so diem hien tai cua ban la:',point)
    if q3.upper() =='Co':
        print("chung ta se den voi cau hoi thu 8")
    else:
        quit()

else:
    print("Sai")
    point = point - point
    print("Sai,cam on ban da den voii chuong trinh")
    quit() 
ans8 = input("Cau8:Loài lưỡng cư nào thường xuất hiện và kêu to sau cơn mưa?\nA.Ếch\nB.Cóc\nC.Nhái\nD.Ễnh ương")
if ans8.upper() == 'A':
    print("Dung")
    point = point +8

else:
    print("Sai")
    point = point - point
    print("Sai,cam on ban da den voii chuong trinh")
    quit()
ans9 = input("Cau 9:Châu lục nào có diện tích lớn nhất?\nA.Châu Á\nB.Châu Mỹ\nC.Châu Phi\nD.Châu Âu")
if ans9.upper() == 'A':
    print("Dung")
    point = point +9
    q4 = input("ban co muon tiep tuc hay khong ")
    print('so diem hien tai cua ban la:',point)
    if q4.upper() =='Co':
        print("chung ta se den voi cau hoi thu 10")
    else:
        quit()
else:
    print("Sai")
    point = point - point
    print("Sai,cam on ban da den voii chuong trinh")
    quit()
    
ans10 = input("Cau 10:Công thức tính diện tích hình chữ nhật:\nA.a+b\nB.(a+b)x2\nC.a x b\nD.a-b")
if ans10.upper() == 'A':
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
 
