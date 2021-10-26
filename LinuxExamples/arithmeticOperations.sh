#!/bin/bash
read expression

printf "%.3f" "$(echo "$expression" | bc -l)"
