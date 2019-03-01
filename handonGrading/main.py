from netmiko import Netmiko
from getpass import getpass

cisco1 = {
    "host": "192.168.153.20",
    "username": "test",
    "password": "test123",
    "device_type": "cisco_ios",
    "secret": "test123", # enable
}

net_connect = Netmiko(**cisco1)
print(net_connect.find_prompt())
net_connect.enable()
output = net_connect.send_command("show run int vlan 1")
print(output)
net_connect.disconnect()
