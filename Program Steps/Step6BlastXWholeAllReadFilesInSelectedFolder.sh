#!/bin/bash
#$ -cwd
#S -v
#$ -b n


cd
cd /home/ws152103/Documents/Project/Allumina
cd $1
cd fasta

mkdir AligmentEditedBlast


#blastx -query /home/ws152103/Documents/Project/Testing_Folder/TestSequences.txt.fasta -out /home/ws152103/Documents/Project/Testing_Folder/TestSequences.txt.fasta.out -outfmt "6 qseqid qacc qlen sseqid evalue  bitscore score " -db mygenome


for f in $(ls *.fasta)
do
        echo $f
        blastx -query $f -out $f.out -outfmt "6 qseqid qacc qlen sseqid evalue  bitscore score qframe" -db /home/ws152103/Documents/Project/Allsequences/mygenome -num_threads 4
done

cd
cd /home/ws152103/Documents/Project/Allumina
cd $2
cd fasta

mkdir AligmentEditedBlast


#blastx -query /home/ws152103/Documents/Project/Testing_Folder/TestSequences.txt.fasta -out /home/ws152103/Documents/Project/Testing_Folder/TestSequences.txt.fasta.out -outfmt "6 qseqid qacc qlen sseqid evalue  bitscore score " -db mygenome


for f in $(ls *.fasta)
do
        echo $f
        blastx -query $f -out $f.out -outfmt "6 qseqid qacc qlen sseqid evalue  bitscore score qframe" -db /home/ws152103/Documents/Project/Allsequences/mygenome -num_threads 4
done





