import json
with open("Lab4/sample-data.json", "r") as file:
    data=json.load(file)
print("Interface Status")
print("=" *80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}")
print("-"*80)
count = 0
for item in data["imdata"]:
    if count>=3:
        break
    attributes=item["l1PhysIf"]["attributes"]
    dn =attributes["dn"]
    descr =attributes["descr"]  
    if not descr:  
        descr =""
    speed =attributes["speed"]
    mtu =attributes["mtu"]
    print(f"{dn:<50} {descr:<20} {speed:<7} {mtu:<6}")
    count+=1 