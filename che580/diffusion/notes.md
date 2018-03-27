Requires
https://huskeypm@bitbucket.org/tompace101/nanopore_diffusion.git
to be installed 
Need to use the che580-sp18 branch 


export LOC=/home/pmke226/sources/nanopore_diffusion/src/
export PYTHONPATH=$PYTHONPATH:$LOC
# cp /home/pmke226/sources/nanopore_diffusion/data/params/postproc/che580-sp18.yaml postproc.yaml
# cp /home/pmke226/sources/nanopore_diffusion/data/params/model/che580-sp18.yaml model.yaml

$ module load fenics.2016.2 
#$ module load gmsh
openmpi/2.0.2(15):ERROR:161: Cannot initialize TCL
gmsh/3.0.6(14):ERROR:161: Cannot initialize TCL
(doesn't seem to matter - gmsh command line works ) 

python $LOC/buildgeom.py mesh.yaml 


python buildgeom.py ../data/params/mesh/che580-sp18.yaml
python geom_mk_msh.py ../data/params/mesh/che580-sp18.yaml
python geom_mk_xml.py ../data/params/mesh/che580-sp18.yaml
python solver_run.py ../data/params/model/che580-sp18.yaml 
 - dirichlet [\#/nm3]
 - can modulate q, 'dirichlet' condition on potential 
surface 11 (or 15) 
 - modulate debye_length ([nm])  

>> ./data/solutions/che580-sp18/conc.pvd
../data/solutions/che580-sp18//che580-sp18/conc*.pvd 

 /home/pmke226/sources/nanopore_diffusion/data/postproc/che580-sp18/che580-sp18/*pdf
there exist postprocessing stuff in 

less /home/pmke226/sources/nanopore_diffusion/data/solutions/che580-sp18/che580-sp18/info.yaml
results: {Deff: 0.0003255893345746322, area_11: 235.40947697362324, area_15: 235.4621751780797,
  free_volume_frac: 0.19634954084936207, totflux_01: -6.296503959359829, totflux_04: -10.49744214531924,


or run it all from 'doit' (hashes, therefore runs those w new timestamp) 






