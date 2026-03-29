#Asilbek Asqarov
#Mohirdev python-darslari
#dars-31

class Shaxs:
    __odamlar_soni = 0
    
    def __init__(self, ism , familiya, tyil, passport):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.__passport = passport
        Shaxs.__odamlar_soni += 1
        
    def get_password(self):
        return self.__passport
    
    def set_password(self, password):
        self.__passport == password
    
    @classmethod
    def get_num_people(cls):
        return cls.__odamlar_soni
    
    def get_yosh(self, yil):
        yosh = yil - self.tyil
        return yosh
    
    def get_info(self):
        info = f"{self.ism} {self.familiya} "
        info += f"Tu'gilgan yili:{self.tyil} "
        return info
     
        
        
class Talaba(Shaxs):
    __talabalar_soni = 0
    
    def __init__(self,ism, familiya, tyil, passport , talaba_id):
        super().__init__(ism, familiya, tyil, passport)
        self.__talaba_id = talaba_id
        Talaba.__talabalar_soni += 1
        
    def get_id(self):
        return self.__talaba_id
    
    def set_id(self, new_id):
        self.__talaba_id = new_id
    
    @classmethod
    def get_num_students(cls):
        return cls.__talabalar_soni
    
odam1 = Shaxs("Anvar", "Hasanov", 2003, "AD12345")   
talaba1 =Talaba("Husan", "Hasanov", 2000, "AD12334", "N100011")
talaba2 =Talaba("Hasan", "Husanov", 2000, "AD112233", "N100017")
    

print(f"Talaba eski id: {talaba1.get_id()}")
talaba1.set_id("N1000123")
print(f"Talaba yangi id: {talaba1.get_id()}")

print(f"Jami odamlar: {Shaxs.get_num_people()}")
print(f"Talabalar soni: {Talaba.get_num_students()}")



