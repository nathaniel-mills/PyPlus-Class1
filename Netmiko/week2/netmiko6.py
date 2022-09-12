from netmiko import ConnectHandler


print ("show prompt from device")

cisco4 = {
	'device_type': 'cisco_ios',
	'host': 'cisco4.lasthop.io',
	'username': 'pyclass',
	'password': '88newclass',
	'secret': '88newclass',
	'session_log': 'my_output.txt',
}
net_connect = ConnectHandler(**cisco4)

print('show prompt')
print(net_connect.find_prompt())

net_connect.config_mode()
print(net_connect.find_prompt())

net_connect.exit_config_mode()
print(net_connect.find_prompt())

net_connect.write_channel('disable\n')
print(net_connect.find_prompt())
time.sleep(2)

output = net_connect.read_channel()
print(output)

net_connect.enable()
print(net_connect.find_prompt())