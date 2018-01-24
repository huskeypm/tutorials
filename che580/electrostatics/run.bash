#SBATCH -p limited # partition (queue) for CHE580 

module load apbs
apbs apbs.in >& out 
tail out 
