#Asilbek Asqarov
#Mohirdev python-darslari
#dars-33-03

filename = "C:/Users/Oliya/Desktop/mohirdev_python_darslar/dars-33/info.txt"
with open(filename, 'a') as file:
    while True:
        info = input(">>> ")
        if not info:
            break
        file.write(info + '\n')
        file.flush() 