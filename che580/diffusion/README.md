Requires
https://huskeypm@bitbucket.org/tompace101/nanopore_diffusion.git
to be installed 

git clone https://huskeypm@bitbucket.org/tompace101/nanopore_diffusion.git
(maybe works? )
Need to use the che580-sp18 branch 

#
# User 
#

export LOC=/home/pmke226/sources/nanopore_diffusion/src/
export PYTHONPATH=$PYTHONPATH:$LOC
export PYTHONPATH=$PYTHONPATH:$LOC/solvers/
export PYTHONPATH=$PYTHONPATH:$LOC/customizations/

module load fenics.2016.2 


python $LOC/buildgeom.py ../data/params/mesh/che580-sp18.yaml
python $LOC/geom_mk_msh.py ../data/params/mesh/che580-sp18.yaml
python $LOC/geom_mk_xml.py ../data/params/mesh/che580-sp18.yaml
python $LOC/solver_run.py ../data/params/model/che580-sp18.yaml 

