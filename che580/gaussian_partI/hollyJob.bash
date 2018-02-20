#!/bin/bash 
#SBATCH -p limited # partition (queue) for CHE580 
module load gaussian/G09 
#g09 h_scrf.com
export FILE=guan
g09 ${FILE}_opt.com 
g09 ${FILE}_scrf.com

