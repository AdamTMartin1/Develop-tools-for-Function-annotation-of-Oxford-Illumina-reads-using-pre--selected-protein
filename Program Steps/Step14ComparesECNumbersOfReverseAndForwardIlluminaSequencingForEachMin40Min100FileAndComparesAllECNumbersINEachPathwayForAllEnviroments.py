#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 12:02:37 2023

@author: ws152103
"""

import pandas as pd
import os
import csv

dictionary=pd.DataFrame(columns=['file', 'pathway', 'COUNT', 'EC', 'ECcount'])
Acetotrophic=pd.DataFrame(columns=['file', 'pathway', 'COUNT', 'EC', 'ECcount'])
Hydrogenotrophic=pd.DataFrame(columns=['file', 'pathway', 'COUNT', 'EC', 'ECcount'])
Methylotrophic=pd.DataFrame(columns=['file', 'pathway', 'COUNT', 'EC', 'ECcount'])
Hydrogenotrophic_Acetotrophic_Methylotrophic=pd.DataFrame(columns=['file', 'pathway', 'COUNT', 'EC', 'ECcount'])


ACEFILL = "False"
HYDFILL = "False"
METHFILL = "False"
THREEFILL = "False"
Folder = ("BEDRIJF_1", "BEDRIJF_2", "Circulaire_kas")
Path = ("Min40Files", "Min100Files")
for PA in Path:
    for FOLD in Folder:
        path = '/home/ws152103/Documents/Project/Allumina/{}/fasta/AligmentEditedBlast/TextFiles/Min20Files/{}/CountingByPathway/'.format(FOLD, PA)
        obj = os.scandir(path)
    
        
        
        for entry in obj:
            if entry.is_dir():
                
            
            
                path2="{}{}/".format(path, entry.name)
                
                files = os.scandir(path2)
                
                
                for file in files: 
                    if 'CountingByPathway.csv' in file.name :
                        path3="{}{}".format(path2, file.name)
                        with open(path3, 'r') as f:
                            DATA = f.read()
                            Split=DATA.split()
                            ACE=Split[1]
                            HYD=Split[3]
                            METH=Split[5]
                            ALLTHREE=Split[7]
                            
            
                    
                    if 'ECNUMBER.csv' in file.name :
                        
                        path3="{}{}".format(path2, file.name) 
                        
                        
                        
                        if 'Acetotrophic.csv' in file.name :
                            
                            with open(path3, 'r') as f:
                                data = f.readlines()
                                
                                for x in range(len(data)):
                                    
                                    pathway="Acetotrophic"
                                    if x != 0:
                                        SplitLine=data[x].split()
                                        EC,ECcount=SplitLine[0],SplitLine[2]
                                        dictionary.loc[len(dictionary.index)] = file.name, pathway, ACE, EC, ECcount
                                        Acetotrophic.loc[len(Acetotrophic.index)] = file.name, pathway, ACE, EC, ECcount
                                        ACEFILL="True"
                                        
                                    
                        if 'Hydrogenotrophic.csv' in file.name :
                            with open(path3, 'r') as f:
                                data = f.readlines()
                                for x in range(len(data)):
                                    pathway="Hydrogenotrophic"
                                    if x != 0:
                                        SplitLine=data[x].split()
    
                                        EC,ECcount=SplitLine[0],SplitLine[2]
                                        dictionary.loc[len(dictionary.index)] = file.name, pathway, HYD, EC, ECcount
                                        Hydrogenotrophic.loc[len(Hydrogenotrophic.index)] = file.name, pathway, ACE, EC, ECcount
                                        HYDFILL="True"
                        
                        if 'Methylotrophic.csv' in file.name :
                            with open(path3, 'r') as f:
                                data = f.readlines()
                                for x in range(len(data)):
                                    pathway="Methylotrophic"
                                    if x != 0:
                                        SplitLine=data[x].split()
                                        EC,ECcount=SplitLine[0],SplitLine[2]
                                        dictionary.loc[len(dictionary.index)] = file.name, pathway, METH, EC, ECcount
                                        Methylotrophic.loc[len(Methylotrophic.index)] = file.name, pathway, ACE, EC, ECcount
                                        METHFILL="True"
                                    
                        if 'Hydrogenotrophic_Acetotrophic_Methylotrophic.csv' in file.name :
                            with open(path3, 'r') as f:
                                
                                data = f.readlines()
                                for x in range(len(data)):
                                    pathway="Hydrogenotrophic_Acetotrophic_Methylotrophic"
                                    if x != 0:
                                        SplitLine=data[x].split()
                                        EC,ECcount=SplitLine[0],SplitLine[2]
                                        dictionary.loc[len(dictionary.index)] = file.name, pathway, METH, EC, ECcount
                                        Hydrogenotrophic_Acetotrophic_Methylotrophic.loc[len(Hydrogenotrophic_Acetotrophic_Methylotrophic.index)] = file.name, pathway, ACE, EC, ECcount
                                        THREEFILL="True"




# create a csv file called test.csv and
# store it a temp variable as outfFileHydrogenotrophicile

OUTPUT = "/home/ws152103/Documents/Project/Spreadsheet/PathwayCounts/ECNumbers/ECNumberedPathway.csv"
with open(OUTPUT, "w") as outfile:
    writer = csv.writer(outfile)
    key_list = list(dictionary.keys())
    limit = len(key_list)
    writer.writerow(dictionary.keys())
    print("GOOD")
    for i in range(len(dictionary)):
        writer.writerow([dictionary[x][i] for x in key_list])   
    
if ACEFILL == "True":
    OUTPUTAcetotrophic = "/home/ws152103/Documents/Project/Spreadsheet/PathwayCounts/ECNumbers/Acetotrophic.csv"
    with open(OUTPUTAcetotrophic, "w") as outfile:
        writerACE = csv.writer(outfile)
        key_list = list(Acetotrophic.keys())
        limit = len(key_list)
        writerACE.writerow(Acetotrophic.keys())
        print("GOOD")
        for i in range(len(Acetotrophic)):
            writerACE.writerow([Acetotrophic[x][i] for x in key_list])  
        
if HYDFILL == "True":
    OUTPUTHydrogenotrophic = "/home/ws152103/Documents/Project/Spreadsheet/PathwayCounts/ECNumbers/Hydrogenotrophic.csv"
    with open(OUTPUTHydrogenotrophic, "w") as outfile:
        writerHYD = csv.writer(outfile)
        key_list = list(Hydrogenotrophic.keys())
        limit = len(key_list)
        writerHYD.writerow(Hydrogenotrophic.keys())
        print("GOOD")
        for i in range(len(Hydrogenotrophic)):
            writerHYD.writerow([Hydrogenotrophic[x][i] for x in key_list])   

if METHFILL == "True":
    OUTPUTMethylotrophic = "/home/ws152103/Documents/Project/Spreadsheet/PathwayCounts/ECNumbers/Methylotrophic.csv"
    with open(OUTPUTMethylotrophic, "w") as outfile:
        writerMETH = csv.writer(outfile)
        key_list = list(Methylotrophic.keys())
        limit = len(key_list)
        writerMETH.writerow(Methylotrophic.keys())
        for i in range(len(Methylotrophic)):
            writerMETH.writerow([Methylotrophic[x][i] for x in key_list])  



if THREEFILL == "True":
    OUTPUTHydrogenotrophic_Acetotrophic_Methylotrophic = "/home/ws152103/Documents/Project/Spreadsheet/PathwayCounts/ECNumbers/Hydrogenotrophic_Acetotrophic_Methylotrophic.csv"
    with open(OUTPUTHydrogenotrophic_Acetotrophic_Methylotrophic, "w") as outfile:
        writerTHREE = csv.writer(outfile)
        key_list = list(Hydrogenotrophic_Acetotrophic_Methylotrophic.keys())
        limit = len(key_list)
        writerTHREE.writerow(Hydrogenotrophic_Acetotrophic_Methylotrophic.keys())
        for i in range(len(Hydrogenotrophic_Acetotrophic_Methylotrophic)):
            writerTHREE.writerow([Hydrogenotrophic_Acetotrophic_Methylotrophic[x][i] for x in key_list])  
            





#print(dictionary)
Array  = dictionary.file
Array = list(set(Array)) 

R1Only = []

ArrayDict=pd.DataFrame(columns=['file', 'R', 'Number'])

for x in Array:
    if x.find('_R1_') != -1 or x.find('_R2_')!= -1:
        for y in range(len(dictionary.file)):
            if dictionary.file[y].find('_R1_') != -1:
                if x == dictionary.file[y]:
                    ArrayDict.loc[len(ArrayDict.index)] = dictionary.file[y], dictionary.file[y], y
                    R1Only.append(dictionary.file[y])
            if dictionary.file[y].find('_R2_') != -1:
                    ChangedName = dictionary.file[y].replace("R2", "R1")  
                    
                    ArrayDict.loc[len(ArrayDict.index)] = dictionary.file[y], ChangedName, y

    
            # Tomorrow Need to play around with THe ARRAY Array aboth as it sperating the files wrong . Change the dataframe that its all
            # based apon to the pathway dataframe. As seen in the csv file
                    
                    
R1Only = list(set(R1Only))     
#print(R1Only)
DoneAlready=[]
COUNT=0
for x in R1Only:
    OUTPUT = "/home/ws152103/Documents/Project/Spreadsheet/PathwayCounts/ECNumbers/SperatedByPathwayAndMin/{}.csv".format(x)
    Output=pd.DataFrame(columns=['file', 'pathway', 'Ec', 'ECCount'])
    with open(OUTPUT, "w") as f:
            Xsplit = x.split("_")
            for y in range(len(ArrayDict.file)):
                ySplit = ArrayDict.file[y].split("_")
                if len(ySplit) == 10:
                    if Xsplit[0] == ySplit[0] and Xsplit[1] == ySplit[1] and Xsplit[2] == ySplit[2] and Xsplit[3] == ySplit[3] and Xsplit[4] == ySplit[4] and Xsplit[6] == ySplit[6] and Xsplit[7] == ySplit[7] and Xsplit[8] == ySplit[8] and Xsplit[9] == ySplit[9]: 
                        
                        Nom=ArrayDict.Number[y]
                        #print(Nom)
                        if dictionary.pathway[Nom] == "Hydrogenotrophic_Acetotrophic_Methylotrophic":
                            Output.loc[len(Output.index)] = dictionary.file[Nom], dictionary.pathway[Nom], dictionary.EC[Nom], dictionary.ECcount[Nom]
                        #DoneAlready.append(ArrayDict.file[y])
                        
                
                else:
                    if Xsplit[0] == ySplit[0] and Xsplit[1] == ySplit[1] and Xsplit[2] == ySplit[2] and Xsplit[3] == ySplit[3] and Xsplit[4] == ySplit[4] and Xsplit[6] == ySplit[6] and Xsplit[7] == ySplit[7]:
                
                        Nom=ArrayDict.Number[y]
                        Output.loc[len(Output.index)] = dictionary.file[Nom], dictionary.pathway[Nom], dictionary.EC[Nom], dictionary.ECcount[Nom]
                    
                    #DoneAlready.append(ArrayDict.file[y])
                    #print(Output)
            
            Output = Output.drop_duplicates()
            
            
            for R in Output.index: 
                f.write(Output.file[R])
                f.write(",")
                f.write(Output.pathway[R])
                f.write(",")
                f.write(Output.Ec[R])
                f.write(",")
                f.write(Output.ECCount[R])
                f.write("\n")
                
              