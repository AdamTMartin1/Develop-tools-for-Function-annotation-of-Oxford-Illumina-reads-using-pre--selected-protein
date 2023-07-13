#!/bin/bash
#$ -cwd
#S -v
#$ -b n

cd
cd /home/ws152103/Documents/Project/Allumina
cd $1
mkdir fasta






for f in $(ls *.fastq)
do
        echo $f
	seqret -sequence $f -outseq fasta/$f.fasta
done
