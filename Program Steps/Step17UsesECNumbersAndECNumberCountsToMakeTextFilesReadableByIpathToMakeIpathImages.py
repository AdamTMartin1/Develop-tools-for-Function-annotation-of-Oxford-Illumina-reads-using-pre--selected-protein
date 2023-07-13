#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 16:57:13 2023

@author: ws152103
"""
import pandas as pd
import os
import csv


Folder = ("BEDRIJF_1", "BEDRIJF_2", "Circulaire_kas")
Path = ("Min40Files", "Min100Files")
largerdictionary=pd.DataFrame(columns=[ 'file', 'EC', 'ECcount'])

for PA in Path:
    for FOLD in Folder:
        path = '/home/ws152103/Documents/Project/Allumina/{}/fasta/AligmentEditedBlast/TextFiles/Min20Files/{}/CountingByPathway/'.format(FOLD, PA)
        obj = os.scandir(path)
    
        
        Enviroment=pd.DataFrame(columns=['file', 'EC', 'ECcount'])
        for entry in obj:
            if entry.is_dir():
                
            
            
                path2="{}{}/".format(path, entry.name)
                
                
                ipath = "{}ipath/".format(path2)
                Found = "False"
                
                            
                files = os.scandir(path2)
                
                for file in files:
                    
                    if 'ipath' in file.name :
                        Found="True"
                        
                if Found !="True":
                    os.makedirs(ipath)
                files = os.scandir(path2)
                for file in files: 
                   
                    
                    if 'ECNUMBER.csv' in file.name :
                        
                        path3="{}{}".format(path2, file.name) 
                        
                        dictionary=pd.DataFrame(columns=[ 'EC', 'ECcount'])
                        if 'Acetotrophic.csv' in file.name  or 'Hydrogenotrophic.csv' in file.name or 'Methylotrophic.csv' in file.name or 'Hydrogenotrophic_Acetotrophic_Methylotrophic.csv' in file.name:
                            
                            with open(path3, 'r') as f:
                                data = f.readlines()
                                for x in range(len(data)):
                                    if x != 0:
                                        SplitLine=data[x].split()
                                        
                                        EC,ECcount=SplitLine[0],SplitLine[2]
                                        dictionary.loc[len(dictionary.index)] =  EC, ECcount
                                        largerdictionary.loc[len(largerdictionary.index)] = file.name, EC, ECcount
                                        Enviroment.loc[len(Enviroment.index)] = file.name,  EC, ECcount
                            
                            
                            path4 = "{}ipath/ipath{}.txt".format(path2, file.name) 
                            with open(path4, 'w') as f:
                                for x in dictionary.index:
                                    if dictionary.EC[x] != "Total":
                                        count = int(dictionary.ECcount[x])
                                        Hundredith = int(count/100)
                                        if Hundredith < 1:
                                            Hundredith = 1
                                            
                                        
                                        
                                           
                                        if "Hydrogenotrophic.csv" in largerdictionary.file[x]:
                                            colour = "#f6ff00"
                                        elif "Acetotrophic.csv" in largerdictionary.file[x]:
                                            colour = "#0099ff"
                                        #elif "Methylotrophic.csv." in largerdictionary.file[x]:
                                           # colour = "#bf00ff"
                                        elif "Hydrogenotrophic_Acetotrophic_Methylotrophic.csv" in largerdictionary.file[x]:
                                            colour = "#ff0080"
                                            
                                        ECSplit = largerdictionary.EC[x].replace("C_", "")
                                        f.write(ECSplit)
                                        f.write(" ")
                                        f.write("W")
                                        f.write(str(Hundredith))
                                        f.write(" ")
                                        f.write(colour)
                                        f.write("\n")    
    
                                
                                path5 ="/home/ws152103/Documents/Project/Ipath/Independent/ipath{}.txt".format(file.name)
                                with open(path5, 'w') as f:
                                    for x in dictionary.index:
                                        if dictionary.EC[x] != "Total":
                                            count = int(dictionary.ECcount[x])
                                            Hundredith = int(count/100)
                                            if Hundredith < 1:
                                                Hundredith = 1
                                            print(largerdictionary.file[x])
                                            if "Hydrogenotrophic.csv" in largerdictionary.file[x]:
                                                colour = "#f6ff00"
                                            if "Acetotrophic.csv" in largerdictionary.file[x]:
                                                colour = "#0099ff"
                                            if "Methylotrophic.csv" in largerdictionary.file[x]:
                                                colour = "#bf00ff"
                                            if "Hydrogenotrophic_Acetotrophic_Methylotrophic.csv" in largerdictionary.file[x]:
                                                colour = "#ff0080"
                                                
                                            ECSplit = largerdictionary.EC[x].replace("C_", "")
                                            f.write(ECSplit)
                                            f.write(" ")
                                            f.write("W")
                                            f.write(str(Hundredith))
                                            f.write(" ")
                                            f.write(colour)
                                            f.write("\n")   
                                            
        EnviromentOutput=pd.DataFrame(columns=[ 'file','EC', 'ECcount'])
        ECSingle = list(set(Enviroment.EC))
        for x in range(len(ECSingle)):
            if len(EnviromentOutput)  != x-1:
                EnviromentOutput.loc[x]= "empty","empty",0
            for y in Enviroment.index:
                if ECSingle[x] == Enviroment.EC[y]:   
                    print(ECSingle[x] , Enviroment.EC[y])
                    Total = int(EnviromentOutput.ECcount[x]) + int(Enviroment.ECcount[y])
                    EnviromentOutput.loc[x] =  Enviroment.file[y], ECSingle[x], Total
                    
        path7 = "/home/ws152103/Documents/Project/Ipath/Enviroment/ipath{}{}.txt".format(PA,FOLD)
        with open(path7, 'w') as f:
            for x in EnviromentOutput.index:
                if EnviromentOutput.EC[x] != "Total":
                    count = int(EnviromentOutput.ECcount[x])
                    Hundredith = int(count/100)
                    if Hundredith < 1:
                        Hundredith = 1
                    
                    if "Hydrogenotrophic.csv" in EnviromentOutput.file[x]:
                        colour = "#f6ff00"
                    if "Acetotrophic.csv" in EnviromentOutput.file[x]:
                        colour = "#0099ff"
                    if "Methylotrophic.csv" in EnviromentOutput.file[x]:
                        colour = "#ff0080"
                    if "Hydrogenotrophic_Acetotrophic_Methylotrophic.csv" in EnviromentOutput.file[x]:
                        colour = "#bf00ff"
                        
                    ECSplit = EnviromentOutput.EC[x].replace("C_", "")
                    f.write(ECSplit)
                    f.write(" ")
                    f.write("W")
                    f.write(str(Hundredith))
                    f.write(" ")
                    f.write(colour)
                    f.write("\n")    
                                    

        
filenames = list(set(largerdictionary.file))

for x in range(len(filenames)):
    
    filenames[x]=filenames[x].replace(".Hydrogenotrophic.txt.ECNUMBER.txt", "")
    filenames[x]=filenames[x].replace(".Acetotrophic.txt.ECNUMBER.txt", "")
    filenames[x]=filenames[x].replace(".Methylotrophic.txt.ECNUMBER.txt", "")
    filenames[x]=filenames[x].replace(".Hydrogenotrophic_Acetotrophic_Methylotrophic.txt.ECNUMBER.txt", "")
    
filenames = list(set(filenames))


for x in filenames:
    path6 ="/home/ws152103/Documents/Project/Ipath/ipath{}".format(x)
    with open(path6, 'w') as f:
        for y in largerdictionary.index:
            if str(x) in str(largerdictionary.file[y]): 
                if largerdictionary.EC[y] != "Total":
                    count = int(largerdictionary.ECcount[y])
                    Hundredith = int(count/100)
                    if Hundredith < 1:
                        Hundredith = 1
                        
                    if "Hydrogenotrophic.csv" in largerdictionary.file[y]:
                        colour = "#f6ff00"
                    elif "Acetotrophic.csv" in largerdictionary.file[y]:
                        colour = "#0099ff"
                    elif "Methylotrophic.csv" in largerdictionary.file[y]:
                        colour = "#bf00ff"
                    elif "Hydrogenotrophic_Acetotrophic_Methylotrophic.csv" in largerdictionary.file[y]:
                        colour = "#ff0080"
                        
                    ECSplit = largerdictionary.EC[y].replace("C_", "")
                    f.write(ECSplit)
                    f.write(" ")
                    f.write("W")
                    f.write(str(Hundredith))
                    f.write(" ")
                    f.write(colour)
                    f.write("\n")    
                    
                    




                                     
                                    
                       


