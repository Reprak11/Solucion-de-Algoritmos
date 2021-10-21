#!/bin/bash
read num1
read num2
if [ $num1 -eq $num2 ] ; then
	echo "X is equal to Y"
elif [ $num1 -gt $num2 ] ; then
	echo "X is greater than Y"
else 
	echo "X is less than Y"
fi	
