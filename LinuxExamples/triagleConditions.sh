#!/bin/bash
read side1
read side2
read side3
if [ $side1 = $side2 ] && [ $side2 = $side3 ] ; then
	echo "EQUILATERAL"
elif [ $side1 != $side2 ] && [ $side1 != $side3 ] && [ $side2 != $side3 ] ; then
	echo "SCALENE"
else
	echo "ISOSCELES"
fi
