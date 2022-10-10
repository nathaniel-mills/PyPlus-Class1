import json
from pprint import pprint


print ("Open the JSON file")

with open('interfaces.json') as f:
	data = json.load(f)
#pprint(data)

print(type(data))
print(len(data))

print(data.keys())

for interface_name, interface_value in data.items():
	#print banner
	print('#' * 12)
	print(interface_name)
	try:
		print(interface_value['ipv4'])
	except KeyError:
		continue
