#Asilbek Asqarov
#Mohirdev python-darslari
#dars-28

class User:
    def __init__(self, username , ism , email, tel_raqam = None):
        self.username = username
        self.ism = ism
        self.email = email
        self.tel_raqam = tel_raqam
    
    def get_info(self):
        info = (f"Foydalanuvchi: {self.username}, ismi: {self.ism}, email: {self.email}")
        if self.tel_raqam:
            info += f", tel: {self.tel_raqam}"
        return info
            
        
        
user1 = User("Asqarbek", "Asilbek Asqarov", "asil@gmail.com")
user2 = User("Hasan13", "Hasan Olimov", "hasan13gmail.com", 9123456)
user3 = User("Husan14", "Husan Olimov", "hasan14gmail.com")

print(user1.get_info())
print(user2.get_info())
print(user3.get_info())
