%chk=testh.chk
%NProcShared=2
# HF/6-31++G(d,p) SCF=Tight SCRF=(PCM,Read,Solvent=Cyclohexane) Test

 geomopt

1 1
H         -0.00000        0.00000        0.00000

TABS=300.0

