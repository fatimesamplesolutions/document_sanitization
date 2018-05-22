import openpyxl
import csv
from collections import defaultdict
from pprint import pprint
import pandas as pd

# Convert the .xlsx file to .csv file
def exel_to_csv(file_to_process):
    workbook = openpyxl.load_workbook(file_to_process)  # DUNS+URL without Telephone Number.xlsx
    # get active sheet
    sheet = workbook.active
    with open('output.csv', 'w', newline="") as csvResult:
        csvWrite = csv.writer(csvResult)
        for row in sheet.rows:
            csvWrite.writerow([cell.value for cell in row])


# remove the first column (DUNS) from the file
def remove_first_column(file_to_process):
    with open(file_to_process,"r") as csvFile:
        csvReader = csv.reader( csvFile )
        with open("urls.csv", "w", newline="") as csvResult:
            csvWrite = csv.writer( csvResult )
            for row in csvReader:
                csvWrite.writerow(row[1:])


# remove WWW part from a url given a csv file
def remove_www(file_to_process):

    columns = defaultdict(list)  # each value in each column is appended to a list

    with open(file_to_process) as f:
        reader = csv.DictReader(f)  # read rows into a dictionary format
        for row in reader:  # read a row as {column1: value1, column2: value2,...}
            for (k, v) in row.items():  # go over each column name and value
                columns[k].append(v)  # append the value into the appropriate list
                # based on column name k

    pprint(columns['URL'])

    res = columns['URL']
    csvfile = "urls_without_www.csv"

    # Assuming res is a flat list
    with open(csvfile, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        for val in res:
            v = val.split('www.')
            v1 = v[-1]
            v1 = str(v1).strip()
            writer.writerow([v1])


# remove duplicate rows from a csv file
def remove_duplicate_rows_using_pandas(file_to_process):
    input_file = pd.read_csv(file_to_process)
    output_file = 'urls_no_dups.csv'
    input_file.drop_duplicates(subset=None, inplace=True)
    input_file.to_csv(output_file, index=False)


# remove duplicated without usind pandas
def remove_duplicate_rows(file_to_process):
    with open(file_to_process,'r') as in_file, open('urls_no_dups.csv','w') as out_file:
        seen = set() # set for fast O(1) amortized lookup
        for line in in_file:
            if line in seen: continue # skip duplicate

            seen.add(line)
            out_file.write(line)



"""Call the function you need by uncommenting it"""
# exel_to_csv('DUNS+URL without Telephone Number.xlsx')
# remove_first_column('output.csv')
# remove_www('urls.csv')
# remove_duplicate_rows_using_pandas('urls_without_www.csv')


