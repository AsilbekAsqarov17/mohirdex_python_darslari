#Asilbek Asqarov
#Mohirdev python-darslari
#dars-34-01

import json


data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}

data_json = json.dumps(data, indent=2)

print("Variable:",data)
print("Json:", data_json)
print("Variable type:",type(data))
print("Json type:",type(data_json))

filename = 'car_data.json'

with open(filename, 'w') as file:
    json.dump(data, file, indent = 4)
    