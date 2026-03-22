#Asilbek Asqarov
#Mohirdev python-darslari 
#dars-14

#task1
bro = {'name' : 'bilol',
       'age' : '19',
       'height' : '182' }
print(f"Do'stimni ismi {bro['name']}, yoshi {bro['age']}, bo'yi {bro['height']}")

#task2
sevimli_taom = {'otash' : 'norin',
                'asil' : 'osh',
                'oybek' : 'manti',
                'bilol' : 'shashlik',
                'akbar' : 'halim'}
print(f"Otabekning sevimli taomi {sevimli_taom['otash']}")
print(f"Asilbekning sevimli taomi {sevimli_taom['asil']}")
print(f"Oybekning sevimli taomi {sevimli_taom['oybek']}")

#task3
lugat = {'integer': 'butun',
         'float' : 'kasrson',
         'double' : 'kasrson2',
         'str' : 'array of chars',
         'if': 'agar',
         'else' : 'yoki'}

#task4
search = input("Enter smth to search: ")
print(lugat.get(search, "Bunday ism mavjud emas"))

#task5
if search in lugat:
    print(f"{search} so'zi {lugat[search]} deb tarjima qilinadi!")
else:
    print("Bunda so'z mavjud emas!")


    
    
