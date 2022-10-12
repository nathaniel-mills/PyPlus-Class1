from netmiko import ConnectHandler


print ("Retrieve running config")

cisco4 = {
	'device_type': 'cisco_ios',
	'host': 'cisco4.lasthop.io',
	'username': 'pyclass',
	'password': '88newclass',
	'secret': '88newclass',
	'session_log': 'my_output.txt',
}
net_connect = ConnectHandler(**cisco4)

print('show run')
net_connect = ConnectHandler(**cisco4)

output = net_connect.send_command('show run')
print(output)

with open('cisco4_config.txt', 'w') as f:
    f.write(output)

from ciscoconfparse import CiscoConfParse

CiscoConfParse("cisco4_config.txt")

cisco_obj = CiscoConfParse("cisco4_config.txt")
print(cisco_obj)

print("BGP PEERS:")
print(cisco_obj.find_objects_w_child(parentspec=r"^interface", childspec=r"^\s+ip address")