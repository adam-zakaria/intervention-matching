# imports

import pandas as pd

# Helper functions


def compare(type='bert'):
    # bert is the default comparsion method
    if type == 'bert':
        return
    if type == 'token_based':
        return


# Main execution


# load the spreadsheets
df0 = pd.read_excel('program_descriptions.xlsx')
df1 = pd.read_excel('interventions.xlsx')

# a column to iterate through
column_name = 'program_descriptions'

# iterate through the cells of a column
for cell in df0[column_name]:
    print(cell)
    # iterate through every cell of a spreadsheet
    for index, row in df1.iterrows():
        for cel in row:
            print(cel)
            similarity = compare(cel)
            # write the similarity score to the last column
