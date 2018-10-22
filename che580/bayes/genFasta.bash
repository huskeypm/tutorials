#P20472 
#Q90YK8
#P02628 
#P02625 
#P02618
#P09227 
#P02621
#P02619


arrayName=( P20472 Q90YK8 P02628 P02625 P02618 P09227 P02621 P02619 )
outName="example.fasta"
echo "" > $outName
for i in "${arrayName[@]}"
do
   echo $i
   lwp-download https://www.uniprot.org/uniprot/$i.fasta  
   cat $i.fasta.txt >> $outName
done
