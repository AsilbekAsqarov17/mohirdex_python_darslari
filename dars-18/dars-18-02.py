#Asilbek Asqarov
#Mohirdev python-darslari 
#dars-18-02

#task2
mahsulotlar = {}
n=1
while True:
    key = input(f"{n} mahsulot nomini kriting: ")
    value = input(f"{key} mahsulot narhini kriting: ")
    mahsulotlar[key] = value
    javob = int(input("Yana mahsulot qo'shasizmi? (ha/yo'q): "))
    if javob =='ha':
        n+=1
        continue
    else:
        break
for key, value in mahsulotlar.items():
    print(f"{key.title()} narhi {value} so'm")