# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 10:36:58 2023

@author: Adam Martin
"""
############Imports ##########

import requests
import sys
import json
from typing import Dict

import pandas as pd

from brendapy import BrendaParser, BrendaProtein
from brendapy.console import console
from brendapy.log import get_logger
from brendapy.taxonomy import Taxonomy


WEBSITE_API = "https://rest.uniprot.org/"

#Helper function to download data
def get_url(url, **kwargs):
    response = requests.get(url, **kwargs);
    
    if not response.ok:
        print(response.text)
        response.raise_for_status()
        sys.exit()
    return response




########### Dataframes ##############
InputFile = r"C:\Users\Adam Martin\OneDrive - University of Dundee\Project\Spreadsheet\UbuntuRedoProteinSequences.xlsx"
Input = pd.read_excel(InputFile)

ProcessingInput = pd.DataFrame(columns=['ShortUniprotAnnotations', 'ShortUniprotUnAnnoted', 'ProteinSequence', 'ECNumber', 'ProteinLength'])



DictPathwayHolder = pd.DataFrame(columns=["Pathway", "ShortUniprotAnnotations", "ShortUniprotUnAnnoted", "Position", 'ECNumber', 'ProteinLength'])
DictWithoutPosition = pd.DataFrame(columns=["Pathway", "ShortUniprotAnnotations", "ShortUniprotUnAnnoted", 'ECNumber', 'ProteinLength'])
ShortenedDictPathwayHolder = pd.DataFrame(columns=["Pathway", "ShortUniprotAnnotations",  "Position", 'ECNumber', 'ProteinLength'])


OutputNoDuplicates = pd.DataFrame(columns=['ShortUniprotAnnotations', 'ShortUniprotAnnotations2', 'ProteinSequence', 'Pathway', 'ECNumber', 'ProteinLength'])

OutputToExcel = pd.DataFrame(columns=['ShortUniprotAnnotations', 'ShortUniprotAnnotations2', 'ProteinSequence', 'Pathway', 'ECNumber', 'ProteinLength'])


########### Processing Data Into Fasta format
for n in range(len(Input)):
    #Used to make fasta file containing all files
    UniprotAnnotations = Input.UniprotAnnotations[n]
    ProteinSequenceHolder= Input.ProteinSequence[n]
    
    UniprotAnnotations = UniprotAnnotations[:10]
    
    UniprotAnnotations = UniprotAnnotations[4:]
    
    UniprotAnnotations = ">"+UniprotAnnotations
    
    UniprotAnnotations= UniprotAnnotations.replace("|", "_")
    
    JoinedSequence= (''.join(ProteinSequenceHolder))
    ShortUniprotUnAnnoted = UniprotAnnotations.replace(">", "_")

    #Used to edit protein sequences to make both txt file types#
    if str(UniprotAnnotations) != "None":
        
        ProcessingInput.loc[len(ProcessingInput.index)] = UniprotAnnotations, ShortUniprotUnAnnoted, JoinedSequence, Input.ECNumber[n], Input.ProteinLength[n]


 
########### Processing Pathways, storing them in DictPathwayHolder along with associated data
for n in range(len(ProcessingInput)):
    Holder = []
    for x in range(len(ProcessingInput.ShortUniprotUnAnnoted)):
        if ProcessingInput.ShortUniprotUnAnnoted[n] == ProcessingInput.ShortUniprotUnAnnoted[x]:
            if Input.Pathway[n] == Input.Pathway[x]: 
                Holder.append(Input.Pathway[n])
            else:
                Holder.append(Input.Pathway[n])
                Holder.append(Input.Pathway[x])
            
    
    Holder = list(dict.fromkeys(Holder))
    Holder= (' '.join(Holder))
    
    if ProcessingInput.ProteinLength[n] > 150:
        DictPathwayHolder.loc[len(DictPathwayHolder.index)] = Holder, ProcessingInput.ShortUniprotAnnotations[n], ProcessingInput.ShortUniprotUnAnnoted[n], n, ProcessingInput.ECNumber[n], ProcessingInput.ProteinLength[n]
        DictWithoutPosition.loc[len(DictWithoutPosition.index)] = Holder, ProcessingInput.ShortUniprotAnnotations[n], ProcessingInput.ShortUniprotUnAnnoted[n], ProcessingInput.ECNumber[n], ProcessingInput.ProteinLength[n]
OutputFile = r"C:\Users\Adam Martin\OneDrive - University of Dundee\Project\Spreadsheet\UbuntuRedoNoUniprotDuplicationsAbove150bp.xlsx"
#DictPathwayHolder.to_excel(OutputFile, index=False) 

result_df = DictWithoutPosition.drop_duplicates()
print(result_df)
result_df.to_excel(OutputFile, index=False) 
########### Removing Duplicate Uniprot and Protein Sequences    
#DuplicateLessShortUniprotAnnotations = list(dict.fromkeys(ProcessingInput.ShortUniprotAnnotations))
#DuplicateLessProteinSequence = list(dict.fromkeys(ProcessingInput.ProteinSequence))



#for n in range(len(DuplicateLessShortUniprotAnnotations)):
    
#    PathwayHolder = []
#    
#    IdHolder = False
#    
#    for x in range(len(DictPathwayHolder.ShortUniprotAnnotations)):
#        if DuplicateLessShortUniprotAnnotations[n] == DictPathwayHolder.ShortUniprotAnnotations[x] and IdHolder != True:
#            PathwayHolder.append(DictPathwayHolder.Pathway[n])
#            IdHolder = True
            
    
    
#    ShortenedDictPathwayHolder.loc[len(ShortenedDictPathwayHolder.index)] = PathwayHolder, DuplicateLessShortUniprotAnnotations[n], n, DictPathwayHolder.ECNumber[n], DictPathwayHolder.ProteinLength[n]
    

    
################# Ouptut dataframe
#for n in range(len(DuplicateLessProteinSequence)): 
#    PathwayCut = "".join(ShortenedDictPathwayHolder.Pathway[n])
#    
#    PathwayCut = PathwayCut.replace(" ", "_")
#    

#    OutputNoDuplicates.loc[len(OutputNoDuplicates.index)] = DuplicateLessShortUniprotAnnotations[n], ShortenedDictPathwayHolder.ShortUniprotAnnotations[n], DuplicateLessProteinSequence[n], PathwayCut, ShortenedDictPathwayHolder.ECNumber[n], ShortenedDictPathwayHolder.ProteinLength[n]
    



########## Opens and outputs to AllSequences Fasta file
#OutputFile = r"/home/ws152103/Documents/Project/Allsequences/UbuntuRedoAllSequences.fasta"
#with open(OutputFile, 'w') as f:
#    for n in range(len(OutputNoDuplicates.ShortUniprotAnnotations)): 
#        # Processing Protein Sequence Size currently 150bp +
#        OutputNoDuplicates.ECNumber[n]= OutputNoDuplicates.ECNumber[n].replace(" ", "_")
#        if OutputNoDuplicates.ProteinLength[n] > 150:
#            #Formating of the allsequences file
#            f.write("\n")
#            f.write("|")
#            f.write(OutputNoDuplicates.Pathway[n])
#            f.write("|")
#            f.write(OutputNoDuplicates.ECNumber[n])
#            f.write("|")
#            f.write("\n")
#            f.write(OutputNoDuplicates.ProteinSequence[n])
#            f.write("\n")
#            f.write("")





###### Excel Spreadsheet export containing all differences completed in this python file
###### Removing Duplicates, Labelling with pathway, only if protein length is over 150bp

#for n in range(len(OutputNoDuplicates)): 
#    # Processing Protein Sequence Size currently 150bp +
#    
#    if OutputNoDuplicates.ProteinLength[n] > 150:
#        OutputToExcel.loc[len(OutputToExcel.index)] = OutputNoDuplicates.ShortUniprotAnnotations[n], OutputNoDuplicates.ShortUniprotAnnotations2[n], OutputNoDuplicates.ProteinSequence[n], OutputNoDuplicates.Pathway[n], OutputNoDuplicates.ECNumber[n], OutputNoDuplicates.ProteinLength[n]

#OutputFile = r"/home/ws152103/Documents/Project/Excel/UbuntuRedoNoUniprotDuplicationsAbove150bp.xlsx"
#OutputToExcel.to_excel(OutputFile, index=False)                