#!/bin/bash
#$ -cwd
#S -v
#$ -b n

#File=/home/ws152103/Documents/Project/Sequence/$1/$3/$2.$3.fasta
#cd /home/ws152103/Documents/Project/Sequence
Folder=$1
cd
cd /home/ws152103/Documents/Project/Allumina/$Folder/fasta/AligmentEditedBlast/TextFiles

Output=/home/ws152103/Documents/Project/Allumina/$Folder/fasta/AligmentEditedBlast/TextFiles/LineCount/CountingNumberLines
rm $Output.txt
sum=0
COUNT=0

mkdir LineCount
for f in $(ls *.txt)
do	
        COUNT=$(wc -l < $f)
        echo $COUNT $f
        sum=`expr $sum + $COUNT`
        cd /home/ws152103/Documents/Project/Allumina/$Folder/fasta/AligmentEditedBlast/TextFiles/LineCount
        echo  $COUNT  $f  >> $Output.txt
        cd
        cd /home/ws152103/Documents/Project/Allumina/$Folder/fasta/AligmentEditedBlast/TextFiles
done
cd
cd /home/ws152103/Documents/Project/Allumina/$Folder/fasta/AligmentEditedBlast/TextFiles/LineCount
echo "Total is " $sum 
echo "Total is " $sum >> $Output.txt



