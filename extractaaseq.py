#!/usr/bin/python

import subprocess
import glob
import os
import sys
import pandas as pd
import re


#Biopython module
from Bio.Seq import Seq, Alphabet, IUPAC
from Bio.Alphabet import IUPAC




def read_file(csv_files):
    dataframe = pd.read_csv(csv_files)
    return dataframe

def fetch_columns_pandas(dataframe, column_number):
    fetched_column = dataframe.ix[:,column_number]
    return fetched_column
    #print(fetched_column)

def describe_dataframe(dataframe):
    table_info = dataframe.shape
    rows, columns = table_info
    return rows, columns


def list_files():
    # Takes automatically current working directory
    path = os.getcwd()
    print(path)


    # We are going to use the file type is csv
    extension = 'csv'

    os.chdir(path)
    list_files = [i for i in glob.glob('*.{}'.format(extension))]
    print(list_files)
    return list_files

def pattern_match(string):
    match = re.search('GCTTGT[ATGC]{21}TGCGGTGGAGGT', string)
    if match:
        return match.group()


def convert_codons_peptide(sequence):
    codons_m = Seq(sequence)
    peptide = codons_m.translate()
    return peptide



def create_new_directory(filename):
    os.mkdir(filename)

csv_files = list_files()
print(csv_files)

#if there are no csv files then print
if not csv_files:
    print("No CSV file found")
    sys.exit()

print('Created a new directory called result_files')
create_new_directory('result_files')

for file in csv_files:
    filename, file_extension = os.path.splitext(file)
    print("Now its processing the file.{}".format(file))
    dataframe = read_file(file)
    protein_info = pd.DataFrame()

    for index, row in dataframe.iterrows():
        sequence = row['Sequence']
        count = row['Count']

        #first_frame_sequence = sequence[1:len(sequence)]
        #second_frame_sequence = sequence[2:len(sequence)]
        #third_frame_sequence = sequence[3:len(sequence)]

        pattern1 = pattern_match(sequence)

        if pattern1 is not None:
            #print("Now its converting the codons for all the frames")
            peptide1 = convert_codons_peptide(pattern1)
            #peptide2 = convert_codons_peptide(first_frame_sequence)
            #peptide3 = convert_codons_peptide(second_frame_sequence)
            #peptide4 = convert_codons_peptide(third_frame_sequence)

            protein_info = protein_info.append({'Peptide1': peptide1, 'pattern': pattern1, 'Count': row['Count']}, ignore_index=True)
		
    protein_info.to_csv('result_files/' + filename + "_result" + '.csv', sep=',', encoding='utf-8')


#write_excel_file(protein_info, 'result_peptide.xlsx')
