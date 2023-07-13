#!/bin/bash
#$ -cwd
#S -v
#$ -b n




cd 
input=$1
cd /home/ws152103/Documents/Project/Allumina/$1/fasta/AligmentEditedBlast
mkdir TextFiles
for x in $(ls *.out); do
	echo $x
	sed 's/$'"/`echo \\\r`/" $x >> TextFiles/$x.txt
done

cd TextFiles
ls




