#!/bin/bash

port=$1

#OUTPUT="$(sudo tcpdump -tnn -c 200 -i s1-eth1  | awk '{print $2}' | tr . ' ' | awk '{print $1"."$2"."$3"."$4}' | sort | uniq -c | awk ' {print $2 "\t" $1 }')"
CAPUTURE="$(sudo timeout 5 tcpdump -tnn -c 100 -i "s1-eth${port}"  | awk -F "." '{print $1"."$2"."$3"."$4}' | sort | uniq -c | sort -nr | awk '$1 > 50')"

echo "${CAPTURE}"

IPs="$(echo $CAPTURE | awk '{print $3"\n"$6}')"
#OUTPUT2="$(echo $OUTPUT | wc -l)"

echo "${IPs}"

#drop_in="$(sudo ovs-ofctl -O OpenFlow13 add-flow s1 "in_port=${port},ip,nw_src=${IPs},actions=drop")"
#drop_out="$(sudo ovs-ofctl -O OpenFlow13 add-flow s1 "in_port=${port} ,ip,nw_dst=${IPs},actions=drop")"

