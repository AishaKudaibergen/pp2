import os
import json

file_path = r"c:\Users\kafka\Documents\Demo\lab4\json\sample-data.json"

with open(file_path, 'r') as json_file:
    data = json.load(json_file)

print("Interface Status")
print("=" * 94)
print(f"{'DN':<52} {'Description':<25} {'Speed':<10} {'MTU':<6}")
print("-" * 50, " ", "-" * 20, " ", "-" * 10, " ", "-" * 6)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    description = attributes.get("descr", "")
    speed = attributes.get("speed", "") 
    mtu = attributes["mtu"]
    print(f"{dn:<52} {description:<25} {speed:<10} {mtu:<6}")