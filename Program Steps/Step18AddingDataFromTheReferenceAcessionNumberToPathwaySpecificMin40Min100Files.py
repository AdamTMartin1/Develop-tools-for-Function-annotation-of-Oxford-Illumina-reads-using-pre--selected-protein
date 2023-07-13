#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 16:07:59 2023

@author: ws152103
"""

import pandas as pd
import os
import csv
import requests
import sys
import re




#WEBSITE_API = "https://rest.uniprot.org/"

#Helper function to download data
def get_url(url, **kwargs):
    response = requests.get(url, **kwargs);
    
    if not response.ok:
        print(response.text)
        response.raise_for_status()
        sys.exit()
    return response




dictionary=pd.DataFrame(columns=['Name1','Name2','Length,''Accession', 'Var1', 'Var2','Var3'])

Folder = ("BEDRIJF_1", "BEDRIJF_2", "Circulaire_kas")
Path = ("Min40Files", "Min100Files")

for PA in Path:
    for FOLD in Folder:
        path = '/home/ws152103/Documents/Project/Allumina/{}/fasta/AligmentEditedBlast/TextFiles/Min20Files/{}/CountingByPathway/'.format(FOLD, PA)
        obj = os.scandir(path)
        for entry in obj:
            if entry.is_dir():
                path2="{}{}/".format(path, entry.name)
                OrganismPath = "{}Organism/".format(path2)
                Found = "False"
                files = os.scandir(path2)
                for file in files: 
                    if 'Organism' in file.name :
                        Found="True" 
                if Found !="True":
                    os.makedirs(OrganismPath)
                files = os.scandir(path2)
                for file in files:
                    if file.is_file():
                       
                        if not 'ECNUMBER.txt' in file.name :
                            if not 'CountingByPathway.txt' in file.name : 
                                path3="{}{}".format(path2, file.name) 
                                dictionary=pd.DataFrame(columns=['Name1','Name2','Length','Accession', 'Evalue', 'Bitscore','Bits'])
                                

                                if 'Acetotrophic.csv' in file.name  or 'Hydrogenotrophic.csv' in file.name or 'Methylotrophic.csv' in file.name or 'Hydrogenotrophic_Acetotrophic_Methylotrophic.csv' in file.name:
                                    print(file.name)
                                    dictionary = pd.read_csv(path3)
        
                                    print("Checkpoint  Dictionary")                
                                    Output=pd.DataFrame(columns=['Name1','Name2','Length','Accession', 'Evalue', 'Bitscore','Bits', 'Organism', 'Taxonomy','Sequence'])               
                                    OUTPUTPath = "{}Organism/Organism{}".format(path2, file.name) 
                                    AC = []
                                    for x in dictionary.index:
                                        
                                        AC.append(dictionary.Accession[x].split('|')[0])
                                      
                                    ACSmall = list(set(AC))
                                    Organism = []
                                    Taxonomy = []
                                    Sequence = []
                                    
                                    for x in range(len(ACSmall)):
                                        
                                        Data= get_url(f"https://rest.uniprot.org/uniprotkb/search?query={ACSmall[x]}&format=fasta")
                                        Data = Data.text
                                        Res=Data.split("OS="[1:])
                                        Res = Res[1].split(" OX=")
                                        Organism.append(Res[0])
                                        Tax = Res[1]
                                        Tax=Tax.split(" ")
                                        Taxonomy.append(Tax[0])
                                        
                                        Length = (len(Tax)-1)
                                        Seq = Tax[Length].replace("\n","")
                                        
                                        Seq = re.split("SV=.",Seq)
                                        
                                        Sequence.append(Seq[1])
                                       
                                    for x in dictionary.index:
                                        for y in range(len(ACSmall)):
                                            
                                            if AC[x] == ACSmall[y]:
                                                
                                                Output.loc[len(Output.index)]=dictionary.Name1[x],dictionary.Name2[x],dictionary.Length[x],dictionary.Accession[x],dictionary.Evalue[x],dictionary.Bitscore[x],dictionary.Bits[x], Organism[y], Taxonomy[y], Sequence[y]
                                    print(Output)
                                    print("Checkpoiint Output Text")
                                    with open(OUTPUTPath, "w") as outfile:
                                        writer = csv.writer(outfile)
                                        key_list = list(Output.keys())
                                        limit = len(key_list)
                                        writer.writerow(Output.keys())
                                        print("GOOD")
                                        for i in range(len(Output)):
                                            writer.writerow([Output[x][i] for x in key_list])   
                                    print("Checkpoiint Output ")
                                    
