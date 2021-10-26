#!/bin/bash
read n
average=0

for(( i=1; i <= $n; i++ ))
do
	read value
	: $[average=$average+$value]
done
printf "%.3f" "$(echo "$average/$n" | bc -l)"
