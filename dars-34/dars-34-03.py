#Asilbek Asqarov
#Mohirdev python-darslari
#dars-34-03

import json

filename = 'C:/Users/Oliya/Desktop/mohirdev_python_darslar/dars-34/students.json'

with open(filename) as file:
    students = json.load(file)

    
for item in students["student"]:
    print(f"{item['name']} {item['lastname']}." f"{item['year']}-year student majoring in" f" Faculty of {item['faculty']} ")
        

