from netmiko import ConnectHandler


print ("show prompt from device")

cisco3 = {
	'device_type': 'cisco_ios',
	'host': 'cisco3.lasthop.io',
	'username': 'pyclass',
	'password': '88newclass',
}
net_connect = ConnectHandler(**cisco3)

config_items = [
	"ip name-server 1.1.1.1",
	"ip name-server 1.0.0.1",
	"ip domain-lookup"
]
print('apply config')
output = net_connect.send_config_set(config_items)
print(output)