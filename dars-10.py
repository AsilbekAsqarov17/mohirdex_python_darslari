#Asilbek Asqarov
#Mohirdev python-darslari 
#dars-10

#task1
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car.lower()=='gm':
        print(car.upper())
    else:
        print(car.title())

#task2
for car in cars:
    if car != 'gm':
        print(car.title())
    else:
        print(car.upper())
#task3
login = input("Ismingiz: ")
if login.lower() == 'admin':
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" )
else:
    print(f"Xush kelibsiz, {login}!" )
    
#task4
num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
if num1==num2:
    print("Numubers equal!")
else:
    print("Not equal")

#task5
number = int(input("Enter number: "))
if number<0:
    print("Manfiy son!")
else:
    print("Musbat son!")

#task6
son = int(input("Enter number: "))
if son<0:
    print("Musbat son kiriting!")
else:
    print(f"{son} son ildizi: {son**0.5}")
