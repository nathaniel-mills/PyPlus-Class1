import json
from pprint import pprint


print ("Open the JSON file")

with open('arp.json') as f:
	data = json.load(f)
pprint(data)

new_arp = data['ipV4Neighbors']

pprint(new_arp)

print(type(new_arp))

print(len(new_arp))

pprint(new_arp[0])

print()
pprint('actual output required for lesson 4')
print()

for arp_data in new_arp:
	#print banner
	print('#' * 12)
	print(arp_data['hwAddress'])
	print(arp_data['address'])
	print()