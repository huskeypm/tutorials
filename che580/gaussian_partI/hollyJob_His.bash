#!/bin/bash 
#SBATCH -p limited # partition (queue) for CHE580 
module load gaussian/G09 
g09 h_scrf.com
g09 histidine_opt.com 
g09 histidine_freq.com

