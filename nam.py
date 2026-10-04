import random
thuong = "abcdefghijklmnopqrstuvwxyz"
hoa = "ABCDEFGHIJKLMNOPQRSTUZWXYZ"
so = "0123456789"
dac_biet = "!@#$%^&*"
tat_ca = thuong + hoa + so + dac_biet

do_dai = int(input("Do dai mkhau"))

if do_dai < 8 :
    print("do dai qua it ")
else:
    print("do dai hop le, bat dau tao mkhau...")
    
    mk = [random.choice(thuong),random.choice(hoa),
        random.choice(so),random.choice(dac_biet)]
    for i in range(do_dai - 4):
        mk.append(random.choice(tat_ca))
    random.shuffle(mk)
    print("".join(mk))