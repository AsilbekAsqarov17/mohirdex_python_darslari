#Asilbek Asqarov
#Mohirdev python-darslari
#dars-22-02

#task2
def talaba_info(ism, familiya, **others):
    others['ism'] = ism
    others['familiya'] = familiya
    return others

talaba1 = talaba_info("Asilbek", "Asqarov", yosh=19, manzil = 'Toshkent', t_yil = 2006)
talaba2 = talaba_info("Asqar", "Asqarov", qiziqishi = 'san\'at')
talaba3 = talaba_info("Asil", "Asqarov")
print(talaba1)
print(talaba2)
print(talaba3)