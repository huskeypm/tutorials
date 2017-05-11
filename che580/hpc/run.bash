module load FEniCS.15
python monteCarloIntegration.py 
mpirun -np 4 python hello.py
python trapSerial.py  0 10 10
mpirun -np 4 python trapParallel.py  0 10 10


