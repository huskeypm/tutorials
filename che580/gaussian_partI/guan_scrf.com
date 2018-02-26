%NProcShared=2
%Chk=guan_opt.chk
#n RHF/STO-3G SCF=Tight SCRF=(PCM,Read,Solvent=Generic) geom=check

 Title

1 1

stoichiometry=C1H4O1  
solventname=methanol
eps=32.63
epsinf=1.758


