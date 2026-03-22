#Asilbek Asqarov
#Mohirdev python-darslari 
#dars-11-04

#task4
mahsulotlar = ['anor', 'uzum', 'olma', 'tarvuz', 'shaftoli', 'somsa', 'shashlik', 'osh', 'asal', 'un']
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"Do'konimizda {mahsulot} bor!")
    else:
        print(f"Do'konimizda {mahsulot} yo'q")
