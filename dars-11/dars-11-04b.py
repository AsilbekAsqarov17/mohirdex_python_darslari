#Asilbek Asqarov
#Mohirdev python-darslari 
#dars-11-04b

#task4b
mahsulotlar = ['anor', 'uzum', 'olma', 'tarvuz', 'shaftoli', 'somsa', 'shashlik', 'osh', 'asal', 'un']
savat = []
bor_mahsulotlar = []
mavjud_emas = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)
if mavjud_emas:
    print("Do'konimizda quyidagi mahsulotlar yo'q:")
    print(mavjud_emas)
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
