#!/bin/bash

shopt -s lastpipe

IP=$1
IP_LOCAL=$2

ssh -n -i /opt/support/support.pem support@$IP "sudo systemctl restart scylla-server"

echo "Waiting for scylla to start on $IP..."

sleep 1
while ! ssh -n -i /opt/support/support.pem support@$IP "nodetool status" | grep -w $IP_LOCAL | grep -w "UN" &> /dev/null
do
	echo "Waiting..."
	sleep 1
done

echo "Scylla is up. We are done"

exit 0

#lcount=`ssh -i /opt/support/support.pem support@$IP "nodetool describecluster" | grep "\[" | wc -l`
#
#if [[ "$lcount" == "1" ]]; then
#	echo "We were victorious!"
#	exit 1
#else
#	exit 0
#fi

