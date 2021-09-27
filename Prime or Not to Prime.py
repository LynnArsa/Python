angka = int(input("Masukkan angka : "))

# Prima = 2, 3, 5, 7, 11, 13, 17, 19, 23 dan 29

if angka == 2 or angka == 3 or angka == 5 or angka == 7:
    print("Prime")
elif angka == 1 :
    print("Not Prime")
# Menambahkan batas input angka 
elif angka > 30:
    print("Diluar Jangkauan")
elif angka % 2 != 0:
    if angka % 3 != 0:
        if angka % 5 != 0:
            if angka % 7 != 0:
                print("Prime")
            else:
                print("Not Prime")
        else:
            print("Not Prime")
    else:
        print("Not Prime")
else:
    print("Not Prime")