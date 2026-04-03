#Asilbek Asqarov
#Mohirdev python-darslari
#dars-34-02

import json

talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""

talaba_dict = json.loads(talaba_json)

print("Ism:", talaba_dict['ism'])
print("Familiya:", talaba_dict['familiya'])

filename = 'talaba.json'

with open(filename, 'w') as file:
    json.dump(talaba_dict, file, indent=4)
    
    
    