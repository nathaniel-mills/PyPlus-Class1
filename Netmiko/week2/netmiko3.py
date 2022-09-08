from netmiko import ConnectHandler


print ("show prompt from device")

cisco4 = {
	'device_type': 'cisco_ios',
	'host': 'cisco4.lasthop.io',
	'username': 'pyclass',
	'password': '88newclass',
}
net_connect = ConnectHandler(**cisco4)

print('show version')
version_output = net_connect.send_command('show version', use_textfsm=True)
print(version_output)

print('show lldp neighbors')
lld_output = net_connect.send_command('show lldp neighbors', use_textfsm=True)
print(lld_output)
print(type(lld_output))
print(lld_output[0]['neighbor_interface'])