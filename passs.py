import random

mkhau= ""
do_dai=int(input("do dai mkhau"))
kktn= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(do_dai):
    mkhau += random.choice(kktn)
    

print(mkhau)