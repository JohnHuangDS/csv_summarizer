import pandas as pd
import glob
import numpy as np
import csv

#load dataframe, index_col = 0 uses 0 column as index
df = pd.read_csv('Data/translink-api-example.csv')
df.rename(columns={'Unnamed: 0': 'Row Number'}, inplace=True)

#get rows and columns
n_rows = df.shape[0]
n_columns = df.shape[1]

#write the title of the csv file
with open('output/update.csv', 'w') as csvFile:

    #declare csv writer, delimiter = ' ' for writing stuff into a once cell
    writer = csv.writer(csvFile, delimiter = ' ')
    #insert file name
    writer.writerow(['File Name : update.csv'])
    #insert number of rows
    writer.writerow(["There are " +str(n_rows) + " rows"])
    #insert number of columns
    writer.writerow(["There are " +str(n_columns) + " columns"])
csvFile.close()

# Create Summary Dictionary
my_dict = {}
for items in df.columns:
    #unique items
    a = df[(items)].unique()
    #sort unique items
    a = np.sort(a)
    #create list of highest and lowest values after sort
    values = [a[0],a[-1]]
    #add list to dictionary
    my_dict.update([ (items, values)])

# Create Summary Dataframe
summary3 = pd.DataFrame.from_dict(my_dict)
summary3 = summary3.rename(index={0: "Lowest-value", 1: "Highest-Value"})

# Write first and last rows to csv
with open('output/update.csv', 'a') as csvfile:
    fieldnames =df.columns
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    #unpack dictionary
    for i in range(2):
        #declare dictionary
        dict1 = {}
        for items in my_dict:
            #append items into dict1
            dict1.update([ (items, my_dict[items][i])])
        writer.writerow(dict1)
    writer_linebreak = csv.writer(csvFile, delimiter = ' ')

# Create a linebreak for the next csv
with open('output/update.csv', 'a') as csvFile:

    #declare csv writer, delimiter = ' ' for writing stuff into a once cell
    writer = csv.writer(csvFile, delimiter = ' ')
    #excute a writerow command, can be list, dictionary, etc.

    #insert linebreak
    writer.writerow([" "])
    #insert number of columns
csvFile.close()
