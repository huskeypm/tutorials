#
# ADMIN
# 
Requires
- git clone https://huskeypm@bitbucket.org/tompace101/nanopore_diffusion.git
- check out the che580-sp18 branch 

#
# User 
#

#Edit this line to match your location for the tutorial files
export DATALOC=~/sources/tutorials/che580/diffusion/data/
#export DATALOC=~/tutorials/che580/diffusion/data/

##export LOC=/home/pmke226/sources/nanopore_diffusion/src/
export SRCLOC=/share/apps/che580/nanopore_diffusion/src
export PYTHONPATH=$PYTHONPATH:$SRCLOC
export PYTHONPATH=$PYTHONPATH:$SRCLOC/solvers/
export PYTHONPATH=$PYTHONPATH:$SRCLOC/customizations/

module load fenics.2016.2 


python $SRCLOC/buildgeom.py $DATALOC/params/mesh/che580-sp18.yaml
python $SRCLOC/geom_mk_msh.py $DATALOC/params/mesh/che580-sp18.yaml
python $SRCLOC/geom_mk_xml.py $DATALOC/params/mesh/che580-sp18.yaml
python $SRCLOC/solver_run.py $DATALOC/params/model/che580-sp18.yaml 
python $SRCLOC/postproc.py $DATALOC/params/postproc/che580-sp18.yaml
AND/OR
doit -f $SRCLOC/dodo.py --db-file $DATALOC/.doit.db
