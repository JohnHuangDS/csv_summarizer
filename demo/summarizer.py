import pandas as pd
import glob
import csv
import re
import numpy as np

def init_summary_csv():
    csv_list = search_csv()
    with open('summary/summary.csv', 'w') as csvFile:
        writer = csv.writer(csvFile, delimiter = ' ')
        writer.writerow(['Total Number of CSV files: '+str(len(csv_list))])
        csvFile.close()
    return("summary.csv initialized")

def search_csv():
    extension = 'csv'

    #grab all results with .csv
    result = glob.glob('data/*.{}'.format(extension))
    return(result)

def my_read_csv(csvname):

    delimiter_list = [';']

    #read file
    try:
        #try loading the csv
        df = pd.read_csv(csvname)

        #if it loads, check if one of these other delimiters is in the first column
        for items in delimiter_list:
            x = re.findall(items, df.columns[0])
            #if there is, read using that item
            if len(x) > 0:
                df = pd.read_csv(csvname, items)

    except:
        #if the csv didnt load, try loading with delimiter
        for items in delimiter_list:
            #try reading with an item in the delimiter list
            try:
                df = pd.read_csv(csvname, items)
            except:
            #if it doesnt load, on to the next
                pass

    return(df)

def write_csv_info(df,csv_name):
    # Check to see if the first column is Row ID
    if df.columns[0] != 'Unnamed: 0':
        index =range(df.shape[0])
        df.insert(0, "Row #", index)
    else:
        pass

    n_rows = df.shape[0]
    n_columns = df.shape[1] - 1


    with open('summary/summary.csv', 'a') as csvFile:

        #declare csv writer, delimiter = ' ' for writing stuff into a once cell
        writer = csv.writer(csvFile, delimiter = ' ')
        #excute a writerow command, can be list, dictionary, etc.

        #insert file name
        writer.writerow(['File Name : '+str(csv_name)])
        #insert number of rows
        writer.writerow(["There are " +str(n_rows) + " rows"])
        #insert number of columns
        writer.writerow(["There are " +str(n_columns) + " columns"])
    csvFile.close()
    return('summary.csv has been updated with ' +str(csv_name) + " title")

def write_csv_rows(df):
# Create Summary Dictionary

    my_dict = {}
    my_dict.update([(0, df.loc[0,:]),(1, df.loc[1,:])])
    summary = pd.DataFrame.from_dict(my_dict)
    summary = summary.T

#need to add an index if df doesnt come with one
    summary = summary.rename(columns={"Unnamed: 0": "Row #"})
    with open('summary/summary.csv', 'a') as csvfile:
        fieldnames =summary.columns
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        #unpack dictionary
        for i in range(2):
            #declare dictionary
            dict1 = {}
            for items in summary.columns:
                #append items into dict1
                dict1.update([ (items, summary[items][i])])
            writer.writerow(dict1)
        writer_linebreak = csv.writer(csvfile, delimiter = ' ')

# Create a linebreak for the next csv
def write_csv_linebreak(df):
    with open('summary/summary.csv', 'a') as csvFile:

        #declare csv writer, delimiter = ' ' for writing stuff into a once cell
        writer = csv.writer(csvFile, delimiter = ' ')
        #excute a writerow command, can be list, dictionary, etc.

        #insert linebreak
        writer.writerow([" "])
        #insert number of columns
    csvFile.close()

# Run this block to produce a summary.csv

csv_list = search_csv()
init_summary_csv()
for items in csv_list:
    #print(items)
    try:
        df = my_read_csv(items)
        write_csv_info(df, items)
        write_csv_rows(df)
        write_csv_linebreak(df)
        print(str(items)+" completed")
    except:
        print(str(items)+" was not included")
