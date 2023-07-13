#!/bin/bash
#$ -cwd
#S -v
#$ -b n

cd
cd /home/ws152103/Documents/Project/ReferenceData
makeblastdb -in AllSequences.fa -dbtype prot -out mygenome -title  'Description of the genome'
