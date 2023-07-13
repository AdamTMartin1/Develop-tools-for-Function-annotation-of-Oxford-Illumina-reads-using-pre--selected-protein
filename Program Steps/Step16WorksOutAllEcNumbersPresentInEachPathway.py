#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 13:18:35 2023

@author: ws152103
"""

import pandas as pd
import os
import csv





Full=pd.DataFrame(columns=['File','ECNumber', 'Count','Count2'])
Acetotrophic=pd.DataFrame(columns=['File','ECNumber', 'Count','Count2'])
Methylotrophic=pd.DataFrame(columns=['File','ECNumber', 'Count','Count2'])
Hydrogenotrophic=pd.DataFrame(columns=['File','ECNumber', 'Count','Count2'])
Hydrogenotrophic_Acetotrophic_Methylotrophic=pd.DataFrame(columns=['File','ECNumber', 'Count','Count2'])
OUTPUT=pd.DataFrame(columns=['File','ECNumber', 'Count','Count2'])
INPUT = '/home/ws152103/Documents/Project/Spreadsheet/PathwayCounts/ECNumbers/SperatedByPathwayAndMin/Comparision/AllComparison.csv'

with open(INPUT, 'r') as f:
    DATA = f.readlines()
    
    for x in range(len(DATA)):
        DATA[x]=DATA[x].replace("\n","")
        DATA[x]=DATA[x].replace(" ","")
        DATA[x]=DATA[x].replace('"',"")
        SplitLine=DATA[x].split(",")
        
        if SplitLine != ['']:
            print(SplitLine)
            if SplitLine[1] != "Total":
                Full.loc[len(Full.index)] = SplitLine[0], SplitLine[1], SplitLine[2],SplitLine[3]
                if 'Acetotrophic' in SplitLine[0]:
                    Acetotrophic.loc[len(Full.index)] = SplitLine[0], SplitLine[1], SplitLine[2],SplitLine[3]
                if 'Methylotrophic' in SplitLine[0]:
                    Methylotrophic.loc[len(Full.index)] = SplitLine[0], SplitLine[1], SplitLine[2],SplitLine[3]
                if 'Hydrogenotrophic' in SplitLine[0]:
                    Hydrogenotrophic.loc[len(Full.index)] = SplitLine[0], SplitLine[1], SplitLine[2],SplitLine[3]
                if 'Hydrogenotrophic_Acetotrophic_Methylotrophic' in SplitLine[0]:
                    Hydrogenotrophic_Acetotrophic_Methylotrophic.loc[len(Full.index)] = SplitLine[0], SplitLine[1], SplitLine[2],SplitLine[3]
        
        
        

path = "/home/ws152103/Documents/Project/Spreadsheet/PathwayCounts/ECNumbers/SperatedByPathwayAndMin/Comparision/ECNumbersPathwayOnly/AllPathways.csv"
with open(path, "w") as t:     
    ECNUMBERAcetotrophic = list(set(Acetotrophic.ECNumber))   
    for x in ECNUMBERAcetotrophic:
        Count =Acetotrophic.index[Acetotrophic['ECNumber'] == x].tolist()
        for y in Count:
            OUTPUT.loc[len(OUTPUT.index)] = Acetotrophic.File[y], Acetotrophic.ECNumber[y], Acetotrophic.Count[y], Acetotrophic.Count2[y]
    path = "/home/ws152103/Documents/Project/Spreadsheet/PathwayCounts/ECNumbers/SperatedByPathwayAndMin/Comparision/ECNumbersPathwayOnly/Acetotrophic.csv"
    with open(path, "w") as f:
        for x in ECNUMBERAcetotrophic:
            y=x.replace("C_", "")
            f.write(y)
            f.write("\n")
            
            t.write(y)
            t.write(" ")
            t.write("\n")
          
    
    
    ECNUMBERMethylotrophic = list(set(Methylotrophic.ECNumber))   
    for x in ECNUMBERMethylotrophic:
        Count =Methylotrophic.index[Methylotrophic['ECNumber'] == x].tolist()
        for y in Count:
            OUTPUT.loc[len(OUTPUT.index)] = Methylotrophic.File[y], Methylotrophic.ECNumber[y], Methylotrophic.Count[y], Methylotrophic.Count2[y]
    path = "/home/ws152103/Documents/Project/Spreadsheet/PathwayCounts/ECNumbers/SperatedByPathwayAndMin/Comparision/ECNumbersPathwayOnly/Methylotrophic.csv"
    with open(path, "w") as f:
        for x in ECNUMBERMethylotrophic:
            y=x.replace("C_","")
            f.write(y)
            f.write("\n")
            
            t.write(y)
            t.write(" ")
            t.write("\n")
            
            
           
            
    ECNUMBERMethylotrophic = list(set(Hydrogenotrophic.ECNumber))   
    for x in ECNUMBERMethylotrophic:
        Count =Hydrogenotrophic.index[Hydrogenotrophic['ECNumber'] == x].tolist()
        for y in Count:
            OUTPUT.loc[len(OUTPUT.index)] = Hydrogenotrophic.File[y], Hydrogenotrophic.ECNumber[y], Hydrogenotrophic.Count[y], Hydrogenotrophic.Count2[y]
    path = "/home/ws152103/Documents/Project/Spreadsheet/PathwayCounts/ECNumbers/SperatedByPathwayAndMin/Comparision/ECNumbersPathwayOnly/Hydrogenotrophic.csv"
    with open(path, "w") as f:
        for x in ECNUMBERMethylotrophic:
            y=x.replace("C_", "")
            f.write(y)
            f.write("\n")
            
            t.write(y)
            t.write(" ")
            t.write("\n")
            
            
    ECNUMBERHydrogenotrophic_Acetotrophic_Methylotrophic = list(set(Hydrogenotrophic_Acetotrophic_Methylotrophic.ECNumber))   
    for x in ECNUMBERHydrogenotrophic_Acetotrophic_Methylotrophic:
        Count =Hydrogenotrophic_Acetotrophic_Methylotrophic.index[Hydrogenotrophic_Acetotrophic_Methylotrophic['ECNumber'] == x].tolist()
        for y in Count:
            OUTPUT.loc[len(OUTPUT.index)] = Hydrogenotrophic_Acetotrophic_Methylotrophic.File[y], Hydrogenotrophic_Acetotrophic_Methylotrophic.ECNumber[y], Hydrogenotrophic_Acetotrophic_Methylotrophic.Count[y], Hydrogenotrophic_Acetotrophic_Methylotrophic.Count2[y]
    path = "/home/ws152103/Documents/Project/Spreadsheet/PathwayCounts/ECNumbers/SperatedByPathwayAndMin/Comparision/ECNumbersPathwayOnly/Hydrogenotrophic_Acetotrophic_Methylotrophic.csv"
    with open(path, "w") as f:
        for x in ECNUMBERHydrogenotrophic_Acetotrophic_Methylotrophic:
            y=x.replace("C_", "")
            f.write(y)
            f.write("\n")
            
            t.write(y)
            t.write(" ")
            t.write("\n")
            
        

OUTPUTPath = '/home/ws152103/Documents/Project/Spreadsheet/PathwayCounts/ECNumbers/SperatedByPathwayAndMin/Comparision/AllComparisonSorted.csv'
with open(OUTPUTPath, "w") as outfile:
    writer = csv.writer(outfile)
    key_list = list(OUTPUT.keys())
    limit = len(key_list)
    writer.writerow(OUTPUT.keys())
    print("GOOD")
    for i in range(len(OUTPUT)):
        writer.writerow([OUTPUT[x][i] for x in key_list])   
        


















