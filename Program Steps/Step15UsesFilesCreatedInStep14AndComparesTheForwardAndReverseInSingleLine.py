#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 11:18:16 2023

@author: ws152103
"""


import pandas as pd
import os
import csv

Individual=pd.DataFrame(columns=['File','ECNumber', 'Count','Count2'])
AllIndividuals=pd.DataFrame(columns=['File','ECNumber', 'Count','Count2'])
path = '/home/ws152103/Documents/Project/Spreadsheet/PathwayCounts/ECNumbers/SperatedByPathwayAndMin/'
obj = os.scandir(path)

for entry in obj:
    if entry.is_file():
        path='/home/ws152103/Documents/Project/Spreadsheet/PathwayCounts/ECNumbers/SperatedByPathwayAndMin/{}'.format(entry.name)
        with open(path, 'r') as f:
            DATA = f.readlines()
            Individual=pd.DataFrame(columns=['File','ECNumber', 'Count','Count2','Found'])
            for x in range(len(DATA)):
                pathway="Methylotrophic"
                SplitLine=DATA[x].split(",")
                
                Same="False"
                for y in Individual.ECNumber:
                    if  y == SplitLine[2]:
                        Line =Individual.loc[Individual.ECNumber== y].index[0]
                        SplitLine[3]=SplitLine[3].replace("\n","")
                        
                        Individual.at[Line,'Count2']=SplitLine[3]
                        Individual.at[Line,'Found']=2
                        Same="True"
                if Same == "False":
                    SplitLine[3] =SplitLine[3].replace("\n", "")
                    
                    Individual.loc[len(Individual.index)] = SplitLine[0], SplitLine[2], SplitLine[3], 0, 1
            print(Individual)
            path2 = '/home/ws152103/Documents/Project/Spreadsheet/PathwayCounts/ECNumbers/SperatedByPathwayAndMin/Comparision/{}.csv'.format(entry.name)
            with open(path2, 'w') as f:  
                f.write("File")
                f.write(",")
                f.write("ECNUMBER")
                f.write(",")
                f.write("Count1")
                f.write(",")
                f.write("Count2")
                f.write("\n")
                    
                for R in Individual.index: 
                    AllIndividuals.loc[len(AllIndividuals.index)] = Individual.File[R], Individual.ECNumber[R], Individual.Count[R], Individual.Count2[R]
                    f.write(str(Individual.File[R]))
                    f.write(",")
                    f.write(str(Individual.ECNumber[R]))
                    f.write(",")
                    f.write(str(Individual.Count[R]))
                    f.write(",")
                    f.write(str(Individual.Count2[R]))
                    f.write("\n")
                    

                

OUTPUT = '/home/ws152103/Documents/Project/Spreadsheet/PathwayCounts/ECNumbers/SperatedByPathwayAndMin/Comparision/AllComparison.csv'
with open(OUTPUT, "w") as outfile:
    writer = csv.writer(outfile)
    key_list = list(AllIndividuals.keys())
    limit = len(key_list)
    writer.writerow(AllIndividuals.keys())
    print("GOOD")
    for i in range(len(AllIndividuals)):
        writer.writerow([AllIndividuals[x][i] for x in key_list])   
        