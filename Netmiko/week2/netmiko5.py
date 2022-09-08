from netmiko import ConnectHandler

print ("show prompt from device")

nxos1 = {
	'device_type': 'cisco_nxos',
	'host': 'nxos1.lasthop.io',
	'username': 'pyclass',
	'password': '88newclass',
}

nxos2 = {
	'device_type': 'cisco_nxos',
        'host': 'nxos2.lasthop.io',
        'username': 'pyclass',
        'password': '88newclass',
}

devices = [nxos1, nxos2]

config_file = "vlan.txt"


for kit in (devices):
	net_connect = ConnectHandler(**kit)
	output = net_connect.send_config_from_file(config_file)
	print(output)
	new_output = net_connect.save_config()
	print(new_output)