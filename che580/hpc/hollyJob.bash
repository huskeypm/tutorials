#!/bin/bash 
#SBATCH --tasks=1
#SBATCH --tasks-per-node=1
##SBATCH --partition=GPU 

sleep 10 
# command will work 
echo "Hello!" 

# command will fail
ls nonexistentFilename
