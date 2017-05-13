#perl -ane '$_=~s/sdie\s(78.54)/sdie VAL/; print $_' apbs.in  > VAL.in 
perl -ane '$_=~s/sdie\s(78.54)/sdie 10/; print $_' apbs.in  > 10.in ; apbs 10.in | grep ELEC > 10.out 
perl -ane '$_=~s/sdie\s(78.54)/sdie 20/; print $_' apbs.in  > 20.in ; apbs 20.in | grep ELEC > 20.out 
perl -ane '$_=~s/sdie\s(78.54)/sdie 30/; print $_' apbs.in  > 30.in ; apbs 30.in | grep ELEC > 30.out 
perl -ane '$_=~s/sdie\s(78.54)/sdie 40/; print $_' apbs.in  > 40.in ; apbs 40.in | grep ELEC > 40.out 
perl -ane '$_=~s/sdie\s(78.54)/sdie 50/; print $_' apbs.in  > 50.in ; apbs 50.in | grep ELEC > 50.out 
perl -ane '$_=~s/sdie\s(78.54)/sdie 60/; print $_' apbs.in  > 60.in ; apbs 60.in | grep ELEC > 60.out 
perl -ane '$_=~s/sdie\s(78.54)/sdie 70/; print $_' apbs.in  > 70.in ; apbs 70.in | grep ELEC > 70.out 
perl -ane '$_=~s/sdie\s(78.54)/sdie 78/; print $_' apbs.in  > 78.in ; apbs 78.in | grep ELEC > 78.out 

