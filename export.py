import json

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

json_string = json.dumps(data, indent=2)

print("data2: ",data)
print("json_string: ",json_string)

