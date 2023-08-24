import os
from netmiko import ConnectHandler
import json

from connection import connection_to_device
import connection 



user= 'akki'
password='cisco'
sec='cisco'

ip ='11.1.1.1'

# Connection to R

router={
    'device_type':'cisco_ios_telnet',
    'ip':'192.168.213.131',
    'username':user,
    'password':password,
    'secret':sec,
    'port': 23
}

try:
    connection_to_device(username=user,password=password,secret=sec,ipadd='192.168.213.131',port=23)
    interfaces = connection.connect.send_command('show ip int brief')
    print('interfaces which are up \n')
    print(interfaces)
    ping_res = connection.connect.send_command(f'ping {ip}', expect_string='R1#', read_timeout=20)
    print(ping_res)
    connection.connect.close()
except Exception as e:
    print(e)
finally:
    print('connection closed')
    
