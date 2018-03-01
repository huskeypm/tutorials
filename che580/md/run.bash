#!/bin/sh
#SBATCH -p limited # partition (queue) for CHE580 
# set max wallclock time 
#SBATCH --time=30:00:00
#SBATCH --tasks-per-node=2
module load NAMD/2.9 

# Run jobs
NP=$SLURM_NTASKS
echo "Running with $NP tasks" 

#export EXEC="mpirun -np $NP /share/apps/NAMD/2.9/Linux-x86_64-ibverbs/namd2"
export EXEC="charmrun ++p $NP ++mpiexec /share/apps/NAMD/2.9/Linux-x86_64-ibverbs/namd2"
# For now, until new version is recompiled 
export EXEC="/share/apps/NAMD/2.9/Linux-x86_64-ibverbs/namd2"

${EXEC} Minimization.conf >& Minimization.out 
${EXEC} Annealing.conf >& Annealing.out 
${EXEC} Equilibration.conf >& Equilibration.out 
#${EXEC} MD.conf >& MD.out 

#module load amber
#cpptraj lys_QwikMD.psf < inp.cpptraj
