%NProc=16
%Mem=40MW
%Chk=hcn_hnc_ts.chk
#p HF/6-31G(d) opt=(TS,CalcFC,noeigen) freq MaxDisk=1GW
 
Hydrogen isocyanide: geometry optimization

0 1
 n
 c   1 cn2     
 h   1 hn3        2 hnc3      
 
cn2         1.200000
hn3         1.300000
hnc3         68.000
 

