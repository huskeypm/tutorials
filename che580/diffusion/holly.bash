#!/bin/bash
#SBATCH -p limited # partition (queue) for CHE580 

#Edit this line to match your location for the tutorial files
export DATALOC=~/sources/tutorials/che580/diffusion/data/
#export DATALOC=~/tutorials/che580/diffusion/data/

##export LOC=/home/pmke226/sources/nanopore_diffusion/src/
export SRCLOC=/share/apps/che580/nanopore_diffusion/src
export PYTHONPATH=$PYTHONPATH:$SRCLOC
export PYTHONPATH=$PYTHONPATH:$SRCLOC/solvers/
export PYTHONPATH=$PYTHONPATH:$SRCLOC/customizations/

module load fenics.2016.2 

# You can edit the yaml files below as specified in the tutorial 
#python $SRCLOC/buildgeom.py $DATALOC/params/mesh/che580-sp18.yaml
#python $SRCLOC/geom_mk_msh.py $DATALOC/params/mesh/che580-sp18.yaml
#python $SRCLOC/geom_mk_xml.py $DATALOC/params/mesh/che580-sp18.yaml
#python $SRCLOC/solver_run.py $DATALOC/params/model/che580-sp18.yaml 
#python $SRCLOC/postproc.py $DATALOC/params/postproc/che580-sp18.yaml
#AND/OR
doit -f $SRCLOC/dodo.py --db-file $DATALOC/.doit.db
