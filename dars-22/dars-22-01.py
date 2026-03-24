#Asilbek Asqarov
#Mohirdev python-darslari
#dars-22-01

#task1
def kopaytma(*sonlar):
    natija = 1
    for son in sonlar:
        natija*=son
    return natija

print(kopaytma(1, 2, 3, 4, 5))
