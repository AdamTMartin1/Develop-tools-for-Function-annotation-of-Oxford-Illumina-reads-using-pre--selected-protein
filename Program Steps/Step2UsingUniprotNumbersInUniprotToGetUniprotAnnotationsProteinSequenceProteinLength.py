# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 11:32:10 2023

@author: Adam Martin
"""

import requests
import sys
import json
from typing import Dict

import pandas as pd

from brendapy import BrendaParser, BrendaProtein
from brendapy.console import console
from brendapy.log import get_logger
from brendapy.taxonomy import Taxonomy


#WEBSITE_API = "https://rest.uniprot.org/"

#Helper function to download data
def get_url(url, **kwargs):
    response = requests.get(url, **kwargs);
    
    if not response.ok:
        print(response.text)
        response.raise_for_status()
        sys.exit()
    return response

InputFile = r"C:\Users\Adam Martin\OneDrive - University of Dundee\Project\Spreadsheet\UbuntuRedoUniprotAccessions.xlsx"

Input = pd.read_excel(InputFile)
Output = pd.DataFrame(columns=['Enzyme', 'Process', 'Pathway', 'ECNumber','UniprotNumbers', 'UniprotAnnotations', 'ProteinSequence', 'ProteinLength'])
Uniprots = Input.UniprotNumbers


data= []
x = 0

 


for n in Uniprots:
    r = get_url(f"https://rest.uniprot.org/uniprotkb/search?query={n}&format=fasta")
    data.append(r.text)
    
    UniprotAnnotations, ProteinSequence = data[x].split('\n')[0], data[x].split('\n')[1:]
    ProteinSequence = "".join(ProteinSequence)
    ProteinLength = len(ProteinSequence)
    Output.loc[len(Output.index)] = [Input.Enzyme[x], Input.Process[x], Input.Pathway[x], Input.ECNumber[x], Input.UniprotNumbers[x], UniprotAnnotations, ProteinSequence, ProteinLength] 
    
    x += 1
    print(Input.ECNumber[x], ProteinLength)
    

#Output.to_excel(r"/home/ws152103/Documents/Project/Excel/UbuntuRedoProteinSequences.xlsx", index=False)        
