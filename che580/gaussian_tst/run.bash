#SBATCH -p limited # partition (queue) for CHE580 
module load gaussian/G09
g09 HCN_HF_631G_Opt.com
g09 HNC_HF_631G_Opt.com
g09 TS_HF_631G_Opt.com
g09 TS_HF_631G_IRC.com


