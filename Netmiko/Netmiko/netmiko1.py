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
output = net_connect.send_command(command, expect_string=r':',
								   strip_prompt=False, strip_command=False)
output += net_connect.send_command('\n', expect_string=r':',
								   strip_prompt=False, strip_command=False)
output += net_connect.send_command('8.8.8.8', expect_string=r':',
								   strip_prompt=False, strip_command=False)
for prompt in range(5):
	output += net_connect.send_command('\n', expect_string=r':',
								   strip_prompt=False, strip_command=False)
print(output)