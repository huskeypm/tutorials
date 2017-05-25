%NProc=16
%Mem=40MW
%Chk=hcn_hnc_ts.chk
#p HF/6-31G(d) SCF=Tight SCRF=(PCM,Read,Solvent=Generic) geom=check
 
Hydrogen isocyanide: geometry optimization

0 1
 
stoichiometry=C1H4O1
solventname=methanol
eps=32.63
epsinf=1.758


