
package require psfgen	 
topology top_all27_prot_lipid.inp	 
#pdbalias residue HIS HSE	 
#pdbalias atom ILE CD1 CD	 
segment U {pdb lys.pdb}	 
coordpdb lys.pdb U	 
guesscoord	 
writepdb fin.pdb	 
writepsf fin.psf 

