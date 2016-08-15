#!/bin/bash

N=$1
# Using GNU parallel -- only with a large box!
seq $N |\
    parallel --pipe -N 50 --round-robin -j50 parallel -j50 --block 10k ./mapper.py |\
    ./reducer.py

# using hadoop-streaming
# seq $N > nums
# /usr/bin/hadoop jar /opt/mapr/hadoop/hadoop-2.7.0/share/hadoop/tools/lib/hadoop-streaming-2.7.0-mapr-1506.jar \
#                 -D mapred.map.tasks=100 \
#                 -D mapred.reduce.tasks=1 \
#                 -files mapper.py,reducer.py \
#                 -cmdenv N=$N \
#                 -mapper mapper.py \
#                 -reducer reducer.py \
#                 -input $(pwd)/nums \
#                 -output $(pwd)/output



