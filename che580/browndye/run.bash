#!/bin/bash
module load pdb2pqr
pdb2pqr --ff=amber N.pdb N.pqr
pdb2pqr --ff=amber M.pdb M.pqr


module load apbs 
apbs M.in >& M.apbslog
apbs N.in >& N.apbslog


pqr2xml < N.pqr > N-atoms.xml
pqr2xml < M.pqr > M-atoms.xml

        
make_rxn_pairs -mol0 M-atoms.xml -mol1 N-atoms.xml -ctypes protein-protein-contacts.xml -dist 6.0 > M-N-pairs.xml
make_rxn_file -pairs M-N-pairs.xml -distance 4.9 -nneeded 3 > M-N-rxns.xml
bd_top input.xml
nam_simulation M-N-simulation.xml 

compute_rate_constant < results.xml 
