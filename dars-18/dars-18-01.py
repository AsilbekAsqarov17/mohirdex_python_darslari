#Asilbek Asqarov
#Mohirdev python-darslari 
#dars-18-01

#task1
mahsulotlar = []
n=1
while True:
    mahsulotlar.append(input(f"{n} mahsulot nomini kriting: "))
    javob = input("Yana mahsulot qo'shasizmi? (ha/yo'q): ")
    if javob =='ha':
        n+=1
        continue
    else:
        break
for mahsulot in mahsulotlar:
    print(mahsulot)