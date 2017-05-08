%NProc=32
%Mem=40MW
%Chk=hcn_hnc_ts.chk
#p HF/6-31G(d) scf=(tight,direct) int=finegrid      
   irc=(calcfc,forward,maxpoints=20,stepsize=10) geom=check
 
HCN <-> HNC isomerization: intrinsic reaction path

0 1

