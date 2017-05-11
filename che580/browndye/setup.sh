#!/bin/bash
module load pdb2pqr
pdb2pqr --ff=amber N.pdb N.pqr

# module load ????
pqr2xml < N.pqr > N-atoms.xml


make_rxn_file -pairs M-N-pairs.xml -distance NDIS -nneeded NPAIR > M-N-rxns.xml
