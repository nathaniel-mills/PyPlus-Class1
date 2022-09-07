from netmiko import ConnectHandler


print ("show prompt from device")

cisco4 = {
	'device_type': 'cisco_ios',
	'host': 'cisco4.lasthop.io',
	'username': 'pyclass',
	'password': '88newclass',
}
net_connect = ConnectHandler(**cisco4)

#print(net_connect.find_prompt())

command = 'ping'
output = net_connect.send_command_timing(command,
								   strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing('\n',
								   strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing('8.8.8.8',
								   strip_prompt=False, strip_command=False)
for prompts in range(5):
	output += net_connect.send_command_timing('\n',
								   strip_prompt=False, strip_command=False)
print(output)