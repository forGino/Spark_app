__author__ = 'gino'

#!/usr/bin/env python

import subprocess
from shlex import split
import time
import json
import simplejson
import sys
import os
from pprint import pprint

#while True:
    #subprocess.call(["ls", "-l"])
    #output = subprocess.check_output(["echo", "Hello World"])
    #print output
    #time.sleep(2)

#target = raw_input("Enter the host address:\n")
#p = subprocess.Popen(['ping', '-c 2', target], stdout=subprocess.PIPE)
#print p.communicate()[0]

#stats = raw_input("Enter the stats dir: ")
#p1 = subprocess.call(['curl', '-X', 'GET', 'http://192.168.200.110:8080/stats/desc/1'])
#output = p1.communicate()[0]
#p2 = json.dumps(output, sort_keys=True, indent=4, separators=(',', ': '))

#p1 = subprocess.Popen(['curl', '-X', 'GET', 'http://192.168.200.110:8080/stats/desc/1'], stdout=subprocess.PIPE).communicate()[0]
#with open("/home/gino/pipe.json") as data_file:
    #data = json.load(data_file)

#curl = ['curl', '-X', 'GET', 'http://192.168.200.110:8080/stats/desc/1']
#json = ['python', '-mjson.tool']
#subprocess.call(curl, '|', json)

#subprocess.call("curl -X GET \"http://192.168.200.110:8080/stats/desc/1\" | python -mjson.tool", shell=True)

stats = raw_input("Enter the stats dir: ")
print "***Statistics of : %s ***\n" % stats
curl = ['curl', '-X', 'GET', 'http://192.168.200.110:8080/stats/%s' % stats]
f = open('pipe.json', 'w')  #Open file for writing
p1 = subprocess.Popen(curl, stdout=subprocess.PIPE).communicate()[0]
#p2 = subprocess.Popen(split("python -m json.tool"), stdin=p1.stdout).communicate()[0]
json.dump(p1, f)    #Save Json formated to file
f.close()   #Close file
#time.sleep(10)

#VISUAL in terminal (DEBUGGING)
f = open('pipe.json', 'r')  #Open file for reading
p3 = json.load(f)   #Load Json file
print p3
f.close()


#f = open('pipe.json', 'w')
#data = str(p2)
#f.seek(5)
#f.write(data)
#f.close()

#f = open("/home/gino/pipe.json", 'wb')
#f.write(p1)

#f.close()
#print json.loads('/home/gino/pipe.json')
