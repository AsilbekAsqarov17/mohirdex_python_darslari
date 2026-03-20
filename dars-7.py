#Asilbek Asqarov
#Mohirdev python-darslari 
#dars-6

#task1
ismlar = ["Asqar", "Bilol", "Botir"]
print(f"Salom {ismlar[0]}, bugun choyxona bormi?")
print(f"{ismlar[1]}, choyxonaga boramizmi?")
print(f"{ismlar[2]}, men choyxonaga keldim")

#task2
sonlar = []
sonlar.append(12)
sonlar.append(17.0)
sonlar.append(-9)
sonlar.append(-3)
sonlar.append(0)

sonlar.append(sonlar[2] + sonlar[3])
sonlar.append(sonlar[1] / sonlar[0])
sonlar.insert(3, 15.5)
sonlar[3] = sonlar[3] + 2 
sonlar.remove(12)
print(sonlar)

#task3
t_shaxslar = ["Amir Temur"]
z_shaxslar = ["luke Nichol"]

print("Men tarixiy shaxslardan {t_shaxslar} bilan, zmaonaviy shaxslardan esa {z_shaxslar} bilan suhbat qilishni istar edim")
#task4
friends = []
friends.append("Otabek")
friends.append("Bilol")
friends.append("Akbar")
friends.append("Botirxo'ja")
friends.append("Izzat")
friends.append("Asadbek")
print("Ro'yxatdagi odamlar:", friends)

friends.remove("Bilol")
friends.remove("Izzat")
print("Mehmonga kelgan odamlar: ",friends)

friends.insert(3, "Asan")
friends.insert(5, "Sarvar")

print("Updated list: ", friends)
#task 5
mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(2))
print("Mehmonlar:",  mehmonlar)



