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

#output = net_connect.send_command_timing('show clock')
#print(output)

for kit in (devices):
	net_connect = ConnectHandler(**kit)
	print(net_connect.find_prompt())
	print(kit)