from ciscoconfparse import CiscoConfParse

CiscoConfParse("bgp_config.txt")

cisco_obj = CiscoConfParse("bgp_config.txt")

#print(cisco_obj)

print("BGP PEERS:")
print(cisco_obj.find_objects(r"neighbor"))