import yaml
from yaml.loader import SafeLoader
from netmiko import ConnectHandler

print ("Open the yaml file")

with open('netmiko.yml') as f:
	data = yaml.load(f, Loader=SafeLoader)
print(data)

print(type(data))

print(data.keys())

target_device = data['cisco3']

print(target_device)

net_connect = ConnectHandler(**target_device)

print(net_connect.find_prompt())