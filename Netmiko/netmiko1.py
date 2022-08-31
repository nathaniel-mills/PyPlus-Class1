from netmiko import ConnectHandler


print ("show prompt from device")

cisco3 = {
	'device_type': 'cisco_ios',
	'host': 'cisco3.lasthop.io',
	'username': 'pyclass',
	'password': '88newclass',
}
net_connect = ConnectHandler(**cisco3)

print(net_connect.find_prompt())