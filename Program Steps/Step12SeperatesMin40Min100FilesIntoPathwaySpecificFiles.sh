#!/bin/bash
#$ -cwd
#S -v
#$ -b n


cd 

Folder=$1
Folder2=$2

cd 
cd /home/ws152103/Documents/Project/Allumina/$Folder/fasta/AligmentEditedBlast/TextFiles/Min20Files/$Folder2
ls
for FILE in $(ls *.txt); do
	echo $FILE
	
	FolderName="${FILE//./}"
	cd CountingByPathway	
	mkdir $FolderName
	cd ..
	TotalOutput=/home/ws152103/Documents/Project/Allumina/$Folder/fasta/AligmentEditedBlast/TextFiles/Min20Files/$Folder2/CountingByPathway/$FolderName/$FILE.CountingByPathway
	OutputAcetotrophic=/home/ws152103/Documents/Project/Allumina/$Folder/fasta/AligmentEditedBlast/TextFiles/Min20Files/$Folder2/CountingByPathway/$FolderName/$FILE.Acetotrophic
	OutputHydrogenotrophic=/home/ws152103/Documents/Project/Allumina/$Folder/fasta/AligmentEditedBlast/TextFiles/Min20Files/$Folder2/CountingByPathway/$FolderName/$FILE.Hydrogenotrophic
	OutputMethylotrophic=/home/ws152103/Documents/Project/Allumina/$Folder/fasta/AligmentEditedBlast/TextFiles/Min20Files/$Folder2/CountingByPathway/$FolderName/$FILE.Methylotrophic	
	OutputAllThree=/home/ws152103/Documents/Project/Allumina/$Folder/fasta/AligmentEditedBlast/TextFiles/Min20Files/$Folder2/CountingByPathway/$FolderName/$FILE.AllThree
	OutputHydrogenotrophic_Acetotrophic_Methylotrophic=/home/ws152103/Documents/Project/Allumina/$Folder/fasta/AligmentEditedBlast/TextFiles/Min20Files/$Folder2/CountingByPathway/$FolderName/$FILE.Hydrogenotrophic_Acetotrophic_Methylotrophic
	echo "STAGE 1 COMPLETE"
	rm $TotalOutput.txt
	rm $OutputAcetotrophic.txt
	rm $OutputHydrogenotrophic.txt
	rm $OutputMethylotrophic.txt
	rm $OutputAllThree.csv
	rm $TotalOutput.csv
	rm $OutputAcetotrophic.csv
	rm $OutputHydrogenotrophic.csv
	rm $OutputMethylotrophic.csv
	rm $OutputAllThree.csv
	rm $OutputHydrogenotrophic_Acetotrophic_Methylotrophic.csv
	echo "Removed Old copy of dont worry about error"
	touch $output.csv
	start=$(date +%s)

	Acetotrophic=0
	Hydrogenotrophic=0
	Methylotrophic=0
	AllThree=0
	LineNumber=0
	Header="Name1,Name2,Length,Accession,Evalue,Bitscore,Bits"
	echo $Header >> $OutputAcetotrophic.csv
	echo $Header >> $OutputHydrogenotrophic.csv
	while read -r Name1 Name2 Length Accesion EValue Bitscore Score; do
		if [[ LineNumber -gt 0 ]]; then
			Found="FALSE"
			
			if [[ "$Accesion" == *"|Acetotrophic|"* ]]; then
		  		Acetotrophic=`expr $Acetotrophic + 1`
		  		
		  		echo $Name1 ","  $Name2 ","  $Length "," $Accesion "," $EValue "," $Bitscore "," $Score >> $OutputAcetotrophic.csv
		  		FOUND="TRUE"
		  	fi
		  	
		  		
			if [[ "$Accesion" == *"|Hydrogenotrophic|"* ]]; then
		  		Hydrogenotrophic=`expr $Hydrogenotrophic + 1`
		  		
		  		echo $Name1 ","  $Name2 ","  $Length "," $Accesion "," $EValue "," $Bitscore "," $Score  >> $OutputHydrogenotrophic.csv
		  		FOUND="TRUE"
		  	fi
		  	
		  	if [[ "$Accesion" == *"|Methylotrophic|"* ]]; then
		  		Methylotrophic=`expr $Methylotrophic + 1`
		  		
		  		echo $Name1 ","  $Name2 ","  $Length "," $Accesion "," $EValue "," $Bitscore "," $Score >> $OutputMethylotrophic.csv
		  		FOUND="TRUE"
		  	fi

			if [[ "$Accesion" == *"|Hydrogenotrophic_Acetotrophic_Methylotrophic|"* ]]; then
		  		AllThree=`expr $AllThree + 1`
		  		echo $Name1 ","  $Name2 ","  $Length "," $Accesion "," $EValue "," $Bitscore "," $Score  >> $OutputHydrogenotrophic_Acetotrophic_Methylotrophic.csv

		  	fi
		fi	
	  	LineNumber=`expr $LineNumber + 1`	
	done < $FILE
	echo "Acetotrophic " $Acetotrophic >> $TotalOutput.csv
	echo "Hydrogenotrophic " $Hydrogenotrophic >> $TotalOutput.csv
	echo "Methylotrophic " $Methylotrophic >> $TotalOutput.csv
	echo "Acetotrophic_Hydrogenotrophic_Methylotrophic  " $AllThree >> $TotalOutput.csv
	end=$(date +%s)
	echo "FINISHED TIME ELAPSED Seconds $(($end-$start))"
done


