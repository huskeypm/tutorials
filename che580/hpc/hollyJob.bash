#!/bin/bash 
#SBATCH -p limited # partition (queue) for CHE580 
#SBATCH --tasks=1
#SBATCH --tasks-per-node=1

sleep 10 
# command will work 
echo "Hello!" 

# command will fail
ls nonexistentFilename
