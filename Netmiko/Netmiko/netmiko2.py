from netmiko import ConnectHandler

print ("show prompt from device")

nxos2 = {
	'device_type': 'cisco_nxos',
        'host': 'nxos2.lasthop.io',
        'username': 'pyclass',
        'password': '88newclass',
		'global_delay_factor': 2,
		'fast_cli': True,
}

net_connect = ConnectHandler(**nxos2)

#print(net_connect.find_prompt())

command = 'show lldp neighbors detail'
output = net_connect.send_command_timing(command,
								   strip_prompt=False, strip_command=False)
print(output)