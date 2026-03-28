#Asilbek Asqarov
#Mohirdev python-darslari
#dars-29

class Avto:
    def __init__(self, model, rang, karobka, narh):
        self.model = model
        self.rang = rang
        self.karobka = karobka
        self.narh = narh
        self.km = 0
        
    def get_model(self):
        return self.model
    
    def get_rang(self):
        return self.rang
    
    def get_karobka(self):
        return self.karobka
    
    def get_narh(self):
        return self.narh
    
    def get_avto_info(self):
        return f"Model: {self.model}, Rang: {self.rang}, Karobka: {self.karobka}, Narh: {self.narh} , Km: {self.km}"
    
    def update_km(self, km):
        self.km += km
        
        
class Avtosalon:
    def __init__(self, salon_nomi, manzil, avtolar= None):
        self.salon_nomi = salon_nomi
        self.manzil = manzil
        self.avtolar = []
        self.avtolar_soni = 0
        
    def get_salon_nomi(self):
        return self.salon_nomi
    
    def get_manzil(self):
        return self.manzil
    
    def add_avto(self, avto):
        self.avtolar.append(avto)
        self.avtolar_soni += 1
    
    def get_avtolar(self):
        return [avto.get_avto_info() for avto in self.avtolar]
    
    def get_avtolar_soni(self):
        return self.avtolar_soni
    
    def get_avtosalon_info(self):
        info = f"Avtosalon Nomi: {self.salon_nomi}, Manzil: {self.manzil}, Avto soni: {self.avtolar_soni}"
        info += f"Sotuvdagi avtolar: {self.get_avtolar()}"
        return info
    
    
    
avto1 = Avto("BMW", "qora", "avtomat", 20000)
avto2 = Avto("Audi", 'qizil', "avtomat", 23000)
avto3 = Avto("GM", "oq", "avtomat", 12000)



avtosalon1 = Avtosalon("AsqarAuto", 'Sebzor')
avtosalon1.add_avto(avto1)
avtosalon1.add_avto(avto2)
avtosalon1.add_avto(avto3)

    
def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]




                