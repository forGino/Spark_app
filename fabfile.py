#!/user/bin/env python


import os
from fabric.api import *

HOST = '192.168.100.114'

env.user = os.getenv('SSH_USER', 'sdn')
env.password = os.getenv('SSH_PASSWORD', 'sdn')

@hosts(HOST)
def ddos_alert(arg):
    #sudo('sudo tcpdump -tnn -c 200 -i s1-eth1  | awk \'{print $2}\' | tr . \' \' | awk \'{print $1"."$2"."$3"."$4}\' | sort | uniq -c | awk \' {print $2 "\t" $1 }\' ')
    sudo('/home/sdn/ddos.sh ' + arg)
