#!/bin/bash
#$ -cwd
#S -v
#$ -b n
cd 

Folder=$1

cd 
cd /home/ws152103/Documents/Project/Allumina/$Folder/fasta/AligmentEditedBlast/TextFiles/
mkdir Min20Files
ls

for FILE in $(ls *.txt); do
	echo $FILE
	output=/home/ws152103/Documents/Project/Allumina/$Folder/fasta/AligmentEditedBlast/TextFiles/Min20Files/$FILE.Min20	
	echo "STAGE 1 COMPLETE"
	rm $output.txt
	echo "Removed Old copy of" $FILE
	touch $output.txt
	start=$(date +%s)
	NameStored=""
	MAX=1
	while read -r Name1 Name2 Length Accesion EValue Bitscore Score Difference; do

		
		if [[ "$Bitscore" != *"."* ]]; then
	  		BitscoreHolder="${Bitscore}0"
	  	fi
	  	
	  		
		if [[ "$Bitscore" == *"."* ]]; then
			BitscoreHolder="${Bitscore//./}"
		fi
		
		if [ $(($BitscoreHolder)) -gt $(($MAX)) ];then
			MAX=$BitscoreHolder
			MAXBIT=$Bitscore
			echo $Name1 "NEW MAX" 	$MAX "  Bitscore" $Bitscore
		fi
		
		if [ $(($BitscoreHolder)) -gt 199 ];then
			if [[ "$PastName1" = "$Name1" ]] && [[ "$PastLength" = "$Length" ]] && [[ "$PastAccesion" = "$Accesion" ]] && [[ "$PastEValue" = "$EValue" ]] && [[ "$PastBitscore" = "$Bitscore" ]] && [[ "$PastScore" = "$Score" ]]; then
				COPY=0
			else
				echo $Name1 $Name2  $Length $Accesion $EValue $Bitscore $Score $Difference>> $output.txt
			fi
		fi 
		
		PastName1=$Name1
		PastLength=$Length
		PastAccesion=$Accesion
		PastEValue=$EValue
		PastBitscore=$Bitscore
		PastScore=$Score
	done < $FILE
	echo "MAX SCORE IN FILE IS"  $MAXBIT
	sed -i "1s/^/The Max Bitscore in this file is $MAXBIT\n/" $output.txt
	end=$(date +%s)
	echo "FINISHED TIME ELAPSED Seconds $(($end-$start))"
	
done
cd Min20Files
ls
