# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 12:23:00 2023

@author: Adam Martin
"""

from typing import Dict

#import pytest

from brendapy import BrendaParser, BrendaProtein
from brendapy.settings import BRENDA_FILE
import pandas as pd

BRENDA_PARSER = BrendaParser()
Output = pd.DataFrame(columns=['Enzyme', 'Process', 'Pathway', 'ECNumber','UniprotNumbers'])
n = 0
    
Input = pd.read_excel(r"/home/ws152103/Documents/Project/Excel/Table4PDF.xlsx")


for EC  in Input.ECNumber:
    EC = EC.replace("E", "")
    EC = EC.replace("C", "")
    EC = EC.replace(" ", "")
    
    
    brenda = BrendaParser()
    proteins = brenda.get_proteins(EC)
    for p in proteins:
        Uniprot = str(proteins[p].uniprot)
        if Uniprot != "None":
            
            Output.loc[len(Output.index)] = [Input.Enzyme[n], Input.Process[n], Input.Pathway[n], Input.ECNumber[n], Uniprot] 
    n +=1 
    print(n)
    

Output.to_excel(r"/home/ws152103/Documents/Project/Excel/UbuntuRedoUniprotAccessions.xlsx", index=False)        




    