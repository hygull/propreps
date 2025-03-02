#!/bin/bash

# ip-192-168-1-107:shell_scripts hygull$ sh while_examples.sh 

counter=0

while [ $counter -le 10 ]
do
	echo "Couner $counter"
	((counter++))
done

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

#!/bin/bash
counter=0

while [ $counter -lt 11 ]; do
	echo "Couner $counter"
	((counter++))
done

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