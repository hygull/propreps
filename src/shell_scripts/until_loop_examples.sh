#!/bin/bash
counter=0

# Run the loop until counter becomes greater than 10
until [ $counter -gt 10 ]; do
	echo "Couner $counter"
	((counter++))
done

# ip-192-168-1-107:shell_scripts hygull$ sh until_loop_examples.sh 
# Couner 0
# Couner 1
# Couner 2
# Couner 3
# Couner 4
# Couner 5
# Couner 6
# Couner 7
# Couner 8
# Couner 9
# Couner 10