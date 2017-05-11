export LD_LIBRARY_PATH=/usr/local/NAMD_2.11_Linux-x86_64-multicore:$LD_LIBRARY_PATH

cp /net/share/shared/Examples_and_Tutorials/namdExample/production30.* .
cp /net/share/shared/Examples_and_Tutorials/namdExample/plb_popcwi.p* .   

/usr/local/bin/namd2 production_iter30.conf
