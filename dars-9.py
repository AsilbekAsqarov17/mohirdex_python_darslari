#Asilbek Asqarov
#Mohirdev python-darslari 
#dars-9

#task1
ismlar = ["Asqar", "Bilol", "Otabek", "Oybek", "Akbar"]
for ism in ismlar:
    print("Salom,", ism)
print(f"Kod {len(ismlar)} marta takrorlandi")

#task2
sonlar = list(range(11, 100, 2))
for son in sonlar:
    print(f"Son: {son}, Kubi: {son**3}")

#task3
kinolar = []
print("5 ta eng sevimli kinolaringiz")
for n in range(5):
    kinolar.append(input(f"{n+1}-kino: "))
print(kinolar)

#task4
odamlar = []
odamlar_soni = int(input("Bugun necha kishi bilan suhbat qildingiz?"))
for n in range(odamlar_soni):
    odamlar.append(input(f"{n+1}-suhbat qilgan odamingiz: "))
print(odamlar)