
from __future__ import print_function

import os
import sys
import operator
from subprocess import Popen
import csv

from matplotlib import pyplot as plt
#from matplotlib import style

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SQLContext, Row

def getSqlContextInstance(sparkContext):
    if ('sqlContextSingletonInstance' not in globals()):
        globals()['sqlContextSingletonInstance'] = SQLContext(sparkContext)
    return globals()['sqlContextSingletonInstance']

def process(rdd):
    sqlContext = getSqlContextInstance(rdd.context)
    df = sqlContext.read.json("/root/data.json")
    df.registerTempTable("dfTable")
    rdd = df
    data = sqlContext.sql("SELECT * FROM dfTable")
    packets = df.map(lambda row: (row.port_no, row.rx_packets))
    return packets

sc = SparkContext(appName="SDN-Monitor")
ssc = StreamingContext(sc, 3)
ssc.checkpoint("checkpoint")
dStream = ssc.textFileStream("/root/data.json")
newStream = dStream.transform(process)
#newStream.pprint()

def please1(a, b):
    a, b = b, a
    return a - b

def please2(a, b):
    a = 0
    b = 0
    return 0 

def ddos(rdd):
   pair = list(rdd)
   if (pair[1] / 3) > 1000:
        #pair[1] = 1000
        Popen('fab ddos_alert:' + str(pair[0]) , shell=True)
   return [pair[0], pair[1]]

def save(rdd):
    pair = list(rdd)
    if pair[0] > 100:
        pair[0] = 10
    values = [pair[0],pair[1]] 
    with open('/root/plot.csv', 'a') as f:
        wr = csv.writer(f)
        wr.writerow(values)
    return pair

#stream2 = newStream.reduceByKeyAndWindow(please1, please2, 4, 2).sortByKey().map(lambda x: x[1] > 1000)

stream2 = newStream.reduceByKeyAndWindow(please1, please2, 6, 3).transform(lambda rdd: rdd.sortByKey(True))
#stream3 = stream2.map(ddos)
#stream2.foreachRDD(lambda rdd: rdd.value())
#stream2.map(save).pprint()
stream2.map(ddos).pprint()

print("START.....")

ssc.start()
ssc.awaitTermination()
