#!/bin/bash 
#SBATCH -p limited # partition (queue) for CHE580 
##SBATCH -N 1 # number of nodes /commented out
##SBATCH -n 1 # number of cores /commented out
#SBATCH --tasks=8  
#SBATCH --tasks-per-node=8

# loading libraries 
module load FEniCS.15

# Figuring out a number of trapezoides we can use 
echo "Running trapParallel.py program on $SLURM_JOB_NUM_NODES nodes with $SLURM_NTASKS tasks"
export NTRAPS=`echo "$SLURM_NTASKS*1000000" | bc`
#echo $NTRAPS


# The 'time' command is used to print the elapsed time.
export NPROCS=1  # vary me, but set only to log base 2 values (1,2,4,8)
/usr/bin/time -p mpirun -np $NPROCS python trapParallel.py  0 10 $NTRAPS 

export NPROCS=8  # vary me, but set only to log base 2 values (1,2,4,8)
/usr/bin/time -p mpirun -np $NPROCS python trapParallel.py  0 10 $NTRAPS 

