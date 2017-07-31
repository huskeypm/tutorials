
module load NAMD/2.9 

# Run jobs
NP=8
charmrun ++p $NP ++mpiexec /share/apps/NAMD/2.9/Linux-x86_64-ibverbs/namd2 step5_production.inp >& steps4.out  
charmrun ++p $NP ++mpiexec /share/apps/NAMD/2.9/Linux-x86_64-ibverbs/namd2 step5_production.inp >& step5.out 

module load amber
cpptraj ../step3_pbcsetup.xplor.ext.psf < inp.cpptraj
