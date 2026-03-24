#Asilbek Asqarov
#Mohirdev python-darslari 
#dars-20

#task1
def user_info(ismi, familiyasi, tugilgan_yili, tugilgan_joyi, email_manzili = None, telefon_raqami = None):
    info = {
        'ismi' : ismi, 
        'familiyasi': familiyasi,
        'yoshi' : 2026 - int(tugilgan_yili),
        'tugilgan_yili' : tugilgan_yili,
        'email_manzili' : email_manzili,
        'telefon_raqami' : telefon_raqami
        }
    return info

user1= user_info("Asilbek", "Asqarov", 2006, "Toshkent", "asilbek@gmail.com", "941234567")
user2 = user_info("Asqar","Asilbek", 1960, "Toshkent")
print("Task1")
print(user1)
print(user2)

#task2
print("\nTask2")
def mijozlar():
    mijozlar= []
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting",end='')
        ismi = input("Ismingiz: ")
        familiyasi = input("Familiyangiz: ")
        tugilgan_yili = input("Tugilgan_yilingiz: ")
        tugilgan_joyi = input("Tugilgan_joyingiz: ")
        email_manzili = input("Email_manzilingiz: ") or None
        telefon_raqami = input("Telefon_raqamingiz: ") or None
        mijozlar.append(user_info(ismi, familiyasi,tugilgan_yili, tugilgan_joyi,email_manzili, telefon_raqami ))
    
        javob = input("Yana mijoz qo'shasizmi? (yes/no): ")
    
        if javob =='no':
            break
    
    for mijoz in mijozlar:
        print(mijoz)
mijozlar()

#task3
print("\nTask3")
def max_num(num1, num2, num3):
    max = num1
    if max< num2:
        max = num2
    if max < num3:
        max= num3
    return max
        
print(max_num(21, 17, 19))

#task4
print("\nTask4")
def circle_info(radius):
    PI = 3.14
    circle_info = {
        'radius' : radius,
        'diametr' : radius*2,
        'perimter' : 2*PI*radius,
        'yuza' : PI*radius**2
        }
    return circle_info
    
print(circle_info(4))

#task5
print("\nTask5")
def isprime(son):
    if son<2:
        return None
    for n in range(2, int(son**0.5)+1):
        if son%n==0:
            return None
    return son

def primes_in_range(min, max):
    tub_sonlar = []
    for n in  range(min,max):
        if isprime(n):
            tub_sonlar.append(n)
    return tub_sonlar
print(primes_in_range(1, 30))
        
#task6
print("\nTask6")
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) +fib(n-2)
print(fib(4))


def fib_numbers(son):
    quantity = 0
    while quantity <son:
        print(fib(quantity))
        quantity+=1
        
fib_numbers(9)
    


