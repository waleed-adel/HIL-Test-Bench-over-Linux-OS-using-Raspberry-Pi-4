#!/bin/sh

set -e
set -m
#make -f "Linux Server"/makefile

sudo ./"Linux Server"/application.out &
python RPC/GRPC_PI_Server/GPIO_write_server.py &

#C_SERVER_ID=$!
#echo "value PID: $C_SERVER_ID"
#echo "INVOKING THE python script"
#sleep 10
#C_SERVER_ID=$!
#sleep 0.001 #sleep for 1 msec
#GRPC_SERVER_ID=$!
#fg $C_SERVER_ID