#!/bin/bash
#$ -cwd
#S -v
#$ -b n


cd 

Folder=$1
Folder2=$2
start=$(date +%s)
cd 
cd /home/ws152103/Documents/Project/Allumina/$Folder/fasta/AligmentEditedBlast/TextFiles/Min20Files/$Folder2/CountingByPathway
Header="ECNumber,Count"

for FOLDER in $(ls); do
	cd $FOLDER
	rm *ECNUMBER*
	echo "Folder" $FOLDER
	for FILE in $(ls *.csv); do 
		if [[ "$FILE" == *"Acetotrophic.csv"* ]] || [[ "$FILE" == *"Hydrogenotrophic.csv"* ]] || [[ "$FILE" == *"Methylotrophic.csv"* ]] || [[ "$FILE" == *"AllThree.csv"* ]]; then
			echo $FILE
			Output=$FILE.ECNUMBER
			echo $Header >> $Output.csv
			StoredEC=()
			StoredCOUNT=(0)
			while read -r Name1 Comma Name2 Comma2 Length Comma3 Accesion Comma4 EValue Comma5 Bitscore Comma6 Score; do
				
				FOUND="FALSE"
				IFS="|" read -a AC <<< $Accesion
				EC=${AC[2]}
				COUNT=0
				for x in ${!StoredEC[@]}; do
					if [[ "${StoredEC[$x]}" == "$EC" ]]; then
						FOUND="TRUE"
						StoredCOUNT[$x]=`expr ${StoredCOUNT[$x]} + 1`
						
					
					fi
				done
				if [[ "$FOUND" == "FALSE" ]]; then
					StoredEC[${#StoredEC[@]}]=$EC
				fi

			done < $FILE
			TOTAL=0
			for x in ${!StoredEC[@]}; do
				if [[ StoredCOUNT[$x] -ne 0 ]]; then
					
					StoredCOUNT[$x]=`expr ${StoredCOUNT[$x]} + 1`	
					echo ${StoredEC[$x]} "," ${StoredCOUNT[$x]} >> $Output.csv
					echo "STORED EC" ${StoredEC[$x]} "Count"  ${StoredCOUNT[$x]} 	
					TOTAL=$(( ${StoredCOUNT[$x]} + $TOTAL ))
				fi
					
			done
				
				echo "Total" $TOTAL  "Line Numbers" $LINENUMBER
				echo  "Total" "," $TOTAL   >> $Output.csv
				
				
		fi
	done
	cd ..
	end=$(date +%s)
	echo "TIME ELAPSED Seconds $(($end-$start))"
	
done
 





