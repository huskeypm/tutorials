
package require psfgen	 
topology top_all27_prot_lipid.inp	 
pdbalias residue HIS HSE	 
pdbalias atom ILE CD1 CD	 
segment U {pdb ile.pdb}	 
coordpdb ile.pdb U	 
guesscoord	 
writepdb fin.pdb	 
writepsf fin.psf 

