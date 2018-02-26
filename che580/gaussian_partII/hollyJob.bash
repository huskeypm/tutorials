#!/bin/bash 
#SBATCH -p limited # partition (queue) for CHE580 
module load gaussian/G09 
export FILE=butadiene
#g09 ${FILE}_opt.com 
g09 ${FILE}_spe.com

