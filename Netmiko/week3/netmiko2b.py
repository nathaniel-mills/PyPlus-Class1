import yaml
from pprint import pprint

device_list = [
	{
		'device_type': 'Cisco IOS-XE',
		'hostname': 'cisco3.lasthop.io',
		'username': 'sonic',
		'password': 'hedgehog'
	},
	{
		'device_type': 'Cisco IOS-XE',
		'hostname': 'cisco4.lasthop.io',
		'username': 'knuckles',
		'password': 'echidnas'
	},
	{
		'device_type': 'Arista vEOS switch',
		'hostname': 'arista1.lasthop.io',
		'username': 'mario',
		'password': 'plumber'
	},
	{
		'device_type': 'Juniper SRX',
		'hostname': 'srx2.lasthop.io',
		'username': 'luigi',
		'password': 'plumber'
	},
	{
		'device_type': 'NX-OSv Switch',
		'hostname': 'nxos1.lasthop.io',
		'username': 'yoshi',
		'password': 'dinosaur'
	}

]


# print(type(device_list))

# print(len(device_list))

# print(device_list[0])

# for devices in device_list:
# #print banner
# 	print('#' * 12)
# #	print(devices)
# 	print(devices['device_type'])
# 	print(devices['hostname'])
# #	break
# 	print('#' * 12)
# 	print()

filename = "outfile.yml"
with open(filename, "wt") as f:
	yaml.dump(device_list, f, default_flow_style=True)