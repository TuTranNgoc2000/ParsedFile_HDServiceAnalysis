import pandas as pd
import ast
import os
import csv
def parse_log(filePath):
    data =[]
    with open(filePath) as f:
        index = 1
        for line in f:
            try: 
                row =ast.literal_eval(line) 
                data.append(row)
            except Exception as e:
            # write to file
                print(e)
                print("Error at line:",index)
            index +=1
    # create DataFrame
    df= pd.DataFrame(data)
    filePathsave="C:/Users/TU/Documents/TuResults/" + filePath.split("/")[-1].split(".")[0]+".tsv"
    df.to_csv(filePathsave,sep="\t",index= False)
    print("Success at: ", filePathsave)

filePaths = [
    "C:/Users/TU/Documents/TuDataset/logt21.txt",
    "C:/Users/TU/Documents/TuDataset/logt22.txt",
    "C:/Users/TU/Documents/TuDataset/logt23.txt",
    "C:/Users/TU/Documents/TuDataset/logt24.txt",
    "C:/Users/TU/Documents/TuDataset/logt25.txt",
    "C:/Users/TU/Documents/TuDataset/logt31.txt",   
    "C:/Users/TU/Documents/TuDataset/logt32.txt",    
]

for filePath in filePaths:
    parse_log(filePath)
# convert user_info txt to tsv

def convertuser_info():
 
    data =[]
    # Open the input and output files
    with open(r'C:\Users\TU\Documents\TuDataset\user_info.txt') as infile:
        # Create a CSV reader with tab delimiter
        reader = csv.reader(infile, delimiter='\t')
        # Iterate over each row in the input file and write it to the output file
        for row in reader:
            data.append(row)
    dfuser= pd.DataFrame(data)
    dfuser.to_csv(r'C:\Users\TU\Documents\TuResults\User\user_info.tsv',sep="\t",index=False) 
    dfuser