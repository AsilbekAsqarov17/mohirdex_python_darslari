#Asilbek Asqarov
#Mohirdev python-darslari 
#dars-11-02

#task2
age = int(input("Enter your age: "))
narh = 0
if(age <=4 or age>=60):
    narh = 'bepul'
elif age<=18:
    narh = 10000
else:
    narh = 20000
print("Narh: ", narh)